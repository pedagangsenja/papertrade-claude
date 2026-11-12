import pandas as pd, numpy as np, json
rng=np.random.default_rng(11)
pd.set_option('display.width',330,'display.max_rows',300,'display.max_colwidth',60)
def muat(f):
    P=pd.read_pickle(f); P=P[P.layak].reset_index(drop=True); P['thn']=P.tarikh//10000
    P['terc']=np.floor(P.groupby('tarikh').atrp.rank(pct=True,method='first')*3).clip(upper=2).astype(int)
    return P
def aturan(P):
    lonjak=(P.f_pos>=0.75)
    return {'TENGAH: tidur (ADX<25, Bollinger separuh bawah) + naik>=4% + volum 1.5x':lonjak&(P.f_ret1>=0.04)&(P.f_vr>=1.5)&(P.f_adx1<25)&(P.f_bbwp<=0.5),
            'KETAT: tidur (ADX<20, Bollinger 30% bawah) + naik>=4% + volum 2x (B05)':lonjak&(P.f_ret1>=0.04)&(P.f_vr>=2)&(P.f_adx1<20)&(P.f_bbwp<=0.3),
            'KUAT: tidur (ADX<20, Bollinger 30% bawah) + naik>=6% + volum 1.5x':lonjak&(P.f_ret1>=0.06)&(P.f_vr>=1.5)&(P.f_adx1<20)&(P.f_bbwp<=0.3),
            'KAWALAN: lonjakan sama TANPA tidur (ADX>=25)':lonjak&(P.f_ret1>=0.04)&(P.f_vr>=1.5)&(P.f_adx1>=25),
            'A06 Golden cross':P['A06 Golden cross MA50/MA200'],'C04 RS>=90 & atas MA50':P['C04 RS >=90 & atas MA50 (keadaan)'],
            'A09 RSI2<10 atas MA200':P['A09 RSI2<10 atas MA200 (Connors)'],'A04 MA10 silang MA20':P['A04 MA10 silang atas MA20'],'A01 MACD silang naik':P['A01 MACD silang naik']}
# ---------- 1. pengesahan pada 498 saham LAIN (stor) ----------
V=muat('panel_stor.pkl')
def baki(P,v): return v-v.groupby([P.tarikh,P.terc]).transform('mean')
print('== PENGESAHAN: 498 saham yang TIADA dalam set 431, isyarat',V.tarikh.min(),'-',V.tarikh.max(),'| asas u20 %.1f r20 %.2f r40 %.2f m16 %.1f'%((V.r20>0).mean()*100,V.r20.mean()*100,V.r40.mean()*100,V.m16.mean()*100))
R=[]
for nm,m in aturan(V).items():
    z=V[m]; 
    R.append(dict(isyarat=nm,n=len(z),saham=z.saham.nunique(),u20=(z.r20>0).mean()*100,r20=z.r20.mean()*100,med20=z.r20.median()*100,L10=baki(V,V.r10*100)[m].mean(),L20=baki(V,V.r20*100)[m].mean(),L40=baki(V,V.r40*100)[m].mean(),L60=baki(V,V.r60*100)[m].mean(),Lu20=baki(V,(V.r20>0)*100.0)[m].mean(),Lm16=baki(V,V.m16*100.0)[m].mean(),kena8=z.kena8.mean()*100))
print(pd.DataFrame(R).set_index('isyarat').round(2).to_string())
# ---------- 2. plasebo anjak-masa 3000 ulangan (set 431) ----------
P=muat('panel_mentah.pkl'); A=aturan(P)
dts=np.sort(P.tarikh.unique()); tks=P.saham.cat.categories; di=np.searchsorted(dts,P.tarikh.to_numpy()); ti=P.saham.cat.codes.to_numpy()
def mat(v,fill=np.nan):
    M=np.full((len(dts),len(tks)),fill); M[di,ti]=np.asarray(v,float); return M
E={k:mat(baki(P,v)) for k,v in {'r20':P.r20*100,'r40':P.r40*100,'ma50':P.x03*100,'ch':P.x01*100}.items()}
print('\n== PLASEBO anjak-masa (3000 ulangan): kebarangkalian lift sebesar ini muncul secara kebetulan ==')
T=len(dts)
for nm in list(A)[:4]:
    S=mat(A[nm],0.0)>0; sb={k:np.nanmean(E[k][S]) for k in E}; bil={k:0 for k in E}; N=3000
    for _ in range(N):
        an=rng.integers(60,T-60,size=S.shape[1]); Sp=np.take_along_axis(S,(np.arange(T)[:,None]-an[None,:])%T,axis=0)
        for k in E:
            if np.nanmean(E[k][Sp])>=sb[k]: bil[k]+=1
    print(nm[:60].ljust(62),{k:(round(sb[k],2),round((bil[k]+1)/(N+1),4)) for k in E})
# ---------- 3. cara pegang/keluar: semua belian lawan belian isyarat TENGAH ----------
XN=json.load(open('panel_mentah.pkl.keluar.json'))
def jadual(z,tajuk):
    R=[]
    for j,kn in enumerate(XN):
        r=z[f'x{j:02d}']; d=z[f'd{j:02d}']; w=r[r>0]; k=r[r<=0]
        R.append(dict(keluar=kn,jgk=r.mean()*100,med=r.median()*100,mng=(r>0).mean()*100,pmng=w.mean()*100,prugi=k.mean()*100,hari=d.mean(),sehari=r.mean()*100/d.mean(),A=r[z.thn<2023].mean()*100,B=r[z.thn>=2023].mean()*100,tanpa5=r[r<r.quantile(0.95)].mean()*100))
    print('\n==',tajuk,'n',len(z)); print(pd.DataFrame(R).set_index('keluar').sort_values('jgk',ascending=False).round(2).to_string())
jadual(P,'SEMUA belian (asas)')
jadual(P[A[list(A)[0]]],'Belian isyarat TENGAH')
jadual(P[A[list(A)[2]]],'Belian isyarat KUAT')
