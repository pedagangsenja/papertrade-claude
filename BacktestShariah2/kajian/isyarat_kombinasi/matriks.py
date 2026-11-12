import pandas as pd, numpy as np, json
pd.set_option('display.width',330,'display.max_rows',300,'display.max_colwidth',70)
XN=json.load(open('panel_mentah.pkl.keluar.json'))
def muat(f):
    P=pd.read_pickle(f); P=P[P.layak].reset_index(drop=True); P['thn']=P.tarikh//10000
    P['terc']=np.floor(P.groupby('tarikh').atrp.rank(pct=True,method='first')*3).clip(upper=2).astype(int)
    lj=(P.f_pos>=0.75)
    P['D01 Saham tidur melonjak (ADX<25, Bollinger sempit, naik>=4%, volum 1.5x)']=lj&(P.f_ret1>=0.04)&(P.f_vr>=1.5)&(P.f_adx1<25)&(P.f_bbwp<=0.5)
    P['D02 Saham tidur melonjak kuat (ADX<20, Bollinger 30% bawah, naik>=6%)']=lj&(P.f_ret1>=0.06)&(P.f_vr>=1.5)&(P.f_adx1<20)&(P.f_bbwp<=0.3)
    return P
P=muat('panel_mentah.pkl'); V=muat('panel_stor.pkl')
SIG=[c for c in P.columns if c[:1] in 'ABCD' and c[1:3].isdigit()]
for D in (P,V):
    for j in range(len(XN)):
        v=D[f'x{j:02d}']*100; D[f'e{j:02d}']=v-v.groupby([D.tarikh,D.terc]).transform('mean')
R=[]
for sn in SIG:
    z=P[P[sn]]; zv=V[V[sn]]
    for j,kn in enumerate(XN):
        r=z[f'x{j:02d}']*100; e=z[f'e{j:02d}']; d=z[f'd{j:02d}']
        yy=r.groupby(z.thn).agg(['mean','size']); yy=yy[yy['size']>=15]; ly=e.groupby(z.thn).mean().reindex(yy.index)
        R.append(dict(masuk=sn,keluar=kn,n=len(z),jgk=r.mean(),med=r.median(),mng=(r>0).mean()*100,pmng=r[r>0].mean(),prugi=r[r<=0].mean(),hari=d.mean(),
            A=r[z.thn<2023].mean(),B=r[z.thn>=2023].mean(),thn_untung=(yy['mean']>0).sum(),thn=len(yy),lift=e.mean(),liftA=e[z.thn<2023].mean(),liftB=e[z.thn>=2023].mean(),thn_lift=(ly>0).sum(),
            terburuk=yy['mean'].min(),tanpa5=r[r<r.quantile(0.95)].mean(),nV=len(zv),jgkV=(zv[f'x{j:02d}']*100).mean() if len(zv) else np.nan,mngV=(zv[f'x{j:02d}']>0).mean()*100 if len(zv) else np.nan,liftV=zv[f'e{j:02d}'].mean() if len(zv) else np.nan))
M=pd.DataFrame(R); M.to_pickle('matriks.pkl')
print('jumlah gabungan',len(M))
ok=M[(M.n>=300)&(M.A>0)&(M.B>0)&(M.thn_untung>=M.thn-1)&(M.liftA>0)&(M.liftB>0)&(M.thn_lift>=5)]
print('lulus tapis ketat (untung kedua-dua separuh, >=6/7 tahun untung, lift positif kedua-dua separuh, lift >=5 tahun):',len(ok))
c=['masuk','keluar','n','jgk','med','mng','pmng','prugi','hari','A','B','thn_untung','terburuk','lift','thn_lift','tanpa5','nV','jgkV','mngV','liftV']
print('\n-- 25 teratas ikut untung purata --'); print(ok.sort_values('jgk',ascending=False)[c].head(25).round(2).to_string(index=False))
print('\n-- 15 teratas ikut kadar menang (antara yang lulus) --'); print(ok.sort_values('mng',ascending=False)[c].head(15).round(2).to_string(index=False))
ok2=ok[(ok.nV>=30)&(ok.jgkV>0)&(ok.liftV>0)]
print('\n-- lulus tapis ketat DAN positif pada 498 saham lain (n>=30) --',len(ok2)); print(ok2.sort_values('jgk',ascending=False)[c].head(25).round(2).to_string(index=False))
print('\n-- asas: beli semua, ikut keluar --'); 
b=[]
for j,kn in enumerate(XN):
    r=P[f'x{j:02d}']*100; rv=V[f'x{j:02d}']*100; b.append(dict(keluar=kn,jgk=r.mean(),mng=(r>0).mean()*100,hari=P[f'd{j:02d}'].mean(),jgkV=rv.mean(),mngV=(rv>0).mean()*100))
print(pd.DataFrame(b).round(2).to_string(index=False))
