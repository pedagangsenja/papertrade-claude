import pandas as pd, numpy as np, json
pd.set_option('display.width',300,'display.max_colwidth',90)
XN=json.load(open('panel_mentah.pkl.keluar.json'))
def dalam(m,N):
    cs=np.cumsum(m,axis=0,dtype=np.int32); o=cs.copy(); o[N:]-=cs[:-N]; return o>0
class S:
    def __init__(s,f):
        P=pd.read_pickle(f); P['k_rs80']=P.rs>=80; P['k_52w']=P.f_j52>=-0.10; s.dts=np.sort(P.tarikh.unique()); di=np.searchsorted(s.dts,P.tarikh.to_numpy()); ti=P.saham.cat.codes.to_numpy(); sh=(len(s.dts),len(P.saham.cat.categories))
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
sq=lambda s:s.K['k_sqon']&s.K['k_sqlepas10']
def mula(s,m):
    p=np.ones_like(m); p[1:]=m[:-1]; return m&~p
# kadar asas lulus pada saham lain: sampel rawak lawan yang lulus tapis utama
D=pd.read_pickle('habis.pkl'); L=pd.read_pickle('habis_lulus.pkl'); rng=np.random.default_rng(3)
CV=V.lap('',np.ones_like(V.ok))['jgk']
def evV(kel,q):
    if kel.startswith('serentak'):
        m=np.ones_like(V.ok)
        for k in q: m=m&V.K[k]
        m=mula(V,m)
    else:
        N=int(kel.split('(')[1].split('h')[0]); m=V.E[q[0]]
        for k in q[1:]: m=V.E[k]&dalam(m,N)
    x=V.X['dua tutup bawah MA50'][m&V.ok]; x=x[~np.isnan(x)]; return len(x),(x.mean() if len(x) else np.nan)
print('\n== adakah lulus tapis utama meramal hasil pada saham lain? ==')
for kel,T in D.dropna(subset=['jgk']).groupby('kel',sort=False):
    sm=T.sample(min(600,len(T)),random_state=1); v=np.array([evV(kel,q) for q in sm.kunci]); g=v[:,0]>=30
    xA=T.A-0.82; xB=T.B-1.78; ok=T[(T.n>=300)&(xA>0.3)&(xB>0.3)&(T.yp>=T.yv-1)]; so=ok.sample(min(600,len(ok)),random_state=1); vo=np.array([evV(kel,q) for q in so.kunci]) if len(so) else np.zeros((0,2)); go=vo[:,0]>=30 if len(vo) else np.array([],bool)
    print('%-26s rawak: purata lain %5.2f, positif lawan kawalan %3.0f%% (n %d) | lulus utama: purata lain %5.2f, positif %3.0f%% (n %d)'%(kel,v[g,1].mean(),(v[g,1]>CV).mean()*100,g.sum(),vo[go,1].mean() if go.any() else np.nan,(vo[go,1]>CV).mean()*100 if go.any() else np.nan,go.sum()))
