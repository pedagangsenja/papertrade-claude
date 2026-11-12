import pandas as pd, numpy as np, json
pd.set_option('display.width',300,'display.max_colwidth',90)
XN=json.load(open('panel_mentah.pkl.keluar.json'))
def dalam(m,N):
    cs=np.cumsum(m,axis=0,dtype=np.int32); o=cs.copy(); o[N:]-=cs[:-N]; return o>0
class S:
    def __init__(s,f):
        P=pd.read_pickle(f); s.dts=np.sort(P.tarikh.unique()); di=np.searchsorted(s.dts,P.tarikh.to_numpy()); ti=P.saham.cat.codes.to_numpy(); sh=(len(s.dts),len(P.saham.cat.categories))
        def M(v,fill,dt=float):
            m=np.full(sh,fill,dtype=dt); m[di,ti]=np.asarray(v,dt); return m
        s.M=M; s.ok=M(P.layak&(P.f_ma50>0),False,bool); s.layak=M(P.layak,False,bool)
        s.X={k:M(P[f'x{XN.index(k):02d}']*100,np.nan) for k in ['dua tutup bawah MA50','TANPA henti: dua tutup bawah MA50','Chandelier 4xATR','biar lari (henti -8% sahaja)','MA10 bawah MA20','pegang 20 hari']}
        s.D=M(P[f'd{XN.index("dua tutup bawah MA50"):02d}'],np.nan)
        s.YR=np.broadcast_to((s.dts//10000)[:,None],sh); s.E={k:M(P[k],False,bool) for k in P.columns if k[:2]=='e_'}; s.K={k:M(P[k],False,bool) for k in P.columns if k[:2]=='k_'}
        s.terc=M(np.floor(P.groupby('tarikh').atrp.rank(pct=True,method='first')*3).clip(upper=2),-1)
    def lap(s,nm,m,k='dua tutup bawah MA50',ok=None):
        m=m&(s.ok if ok is None else ok); x=s.X[k][m]; g=~np.isnan(x); x=x[g]; y=s.YR[m][g]
        if len(x)==0: return dict(nama=nm,n=0)
        yy=pd.Series(x).groupby(y).mean()
        return dict(nama=nm,n=len(x),jgk=x.mean(),med=np.median(x),mng=(x>0).mean()*100,pmng=x[x>0].mean(),prugi=x[x<=0].mean(),A=x[y<2023].mean() if (y<2023).any() else np.nan,B=x[y>=2023].mean(),thn=str([round(float(v),1) for v in yy.values]))
P=S('panel_mentah.pkl'); V=S('panel_stor.pkl')
def dua(nm,fn,k='dua tutup bawah MA50'):
    a=P.lap(nm,fn(P),k); b=V.lap(nm,fn(V),k); a['nV']=b['n']; a['jgkV']=b.get('jgk',np.nan); a['mngV']=b.get('mng',np.nan); return a
R=[dua('KAWALAN mana-mana hari atas MA50',lambda s:np.ones_like(s.ok)),
   dua('gap naik 2% (tunggal)',lambda s:s.E['e_gap']),dua('MA20 silang MA50 (tunggal)',lambda s:s.E['e_ma2050']),dua('silang atas MA50 (tunggal)',lambda s:s.E['e_c50'])]
for N in (5,10,20,40):
    R.append(dua(f'gap naik 2% dalam {N}h -> MA20 silang MA50',lambda s,N=N:s.E['e_ma2050']&dalam(s.E['e_gap'],N)))
R.append(dua('MA20 silang MA50 TANPA gap dalam 20h',lambda s:s.E['e_ma2050']&~dalam(s.E['e_gap'],20)))
for N in (5,10,20):
    R.append(dua(f'gap naik 2% dalam {N}h -> tutup silang atas MA50',lambda s,N=N:s.E['e_c50']&dalam(s.E['e_gap'],N)))
R.append(dua('gap naik 2% dalam 10h -> golden cross',lambda s:s.E['e_gc']&dalam(s.E['e_gap'],10)))
R.append(dua('gap naik 2% dalam 20h -> MA10 silang MA20',lambda s:s.E['e_ma1020']&dalam(s.E['e_gap'],20)))
R.append(dua('gap naik 2% dalam 20h -> MACD silang naik',lambda s:s.E['e_macd']&dalam(s.E['e_gap'],20)))
sq=lambda s:s.K['k_sqon']&s.K['k_sqlepas10']
def mula(s,m):
    p=np.ones_like(m); p[1:]=m[:-1]; return m&~p
R.append(dua('squeeze ON + squeeze lepas(10h) sahaja (hari pertama)',lambda s:mula(s,sq(s))))
R.append(dua('squeeze kedua + tutup>MA200',lambda s:mula(s,sq(s)&s.K['k_c200'])))
R.append(dua('squeeze kedua + MA50>MA200',lambda s:mula(s,sq(s)&s.K['k_ma50200'])))
R.append(dua('squeeze kedua + MA50>MA200 + atas PSAR',lambda s:mula(s,sq(s)&s.K['k_ma50200']&s.K['k_psar'])))
R.append(dua('squeeze kedua + MA50>MA200 + MACD hijau',lambda s:mula(s,sq(s)&s.K['k_ma50200']&s.K['k_macd'])))
R.append(dua('undur RSI2<10 -> gap naik 2% -> RSI silang 50 (5h)',lambda s:s.E['e_rsi50']&dalam(s.E['e_gap']&dalam(s.E['e_rsi2'],5),5)))
print(pd.DataFrame(R).round(2).to_string(index=False))
print('\n== calon utama dengan cara jual lain ==')
c1=lambda s:s.E['e_ma2050']&dalam(s.E['e_gap'],20); c2=lambda s:mula(s,sq(s)&s.K['k_ma50200'])
for nm,fn in (('gap 20h -> MA20 silang MA50',c1),('squeeze kedua + MA50>MA200',c2)):
    print(pd.DataFrame([dua(nm+' | '+k,fn,k) for k in P.X]).round(2).to_string(index=False))
# kelebihan terkawal hari x tercile ATR untuk calon utama
for nm,fn in (('gap 20h -> MA20 silang MA50',c1),('squeeze kedua + MA50>MA200',c2)):
    for s,lab in ((P,'utama'),(V,'lain')):
        df=pd.DataFrame({'t':np.broadcast_to(np.arange(s.ok.shape[0])[:,None],s.ok.shape)[s.ok],'q':s.terc[s.ok],'x':s.X['dua tutup bawah MA50'][s.ok],'m':fn(s)[s.ok]}).dropna()
        df['e']=df.x-df.groupby(['t','q']).x.transform('mean'); print(nm,lab,'| kelebihan lawan saham atas MA50 hari sama & ATR sama: %.2f (n %d)'%(df.e[df.m].mean(),df.m.sum()))
# Kadar asas rawak pada saham lain: lihat semak3.py.
