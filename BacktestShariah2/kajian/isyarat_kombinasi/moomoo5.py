"""Tinjauan (BUKAN pradaftar): 5 isyarat Moomoo pengguna + gabungan, lift atas beli-setiap-bar pada keluar sama."""
import os
import numpy as np, pandas as pd, itertools
from numpy.lib.stride_tricks import sliding_window_view as swv
AKAR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+'/'; H=126; KOS=0.005; HENTI=0.08
d=pd.concat([pd.read_csv(AKAR+f'data_mentah/dataset_{s}.csv') for s in ('S1','S2','S3','S4')]).drop_duplicates(['ticker','date']).sort_values(['ticker','date'])
def wilder(s,n): return s.ewm(alpha=1/n,adjust=False,min_periods=n).mean()
def silang(a,b): return (a>b)&(a.shift()<=b.shift())
def dalam(ev,n): return ev.rolling(n).max().fillna(0).astype(bool)
def pertama(m):
    k=m.argmax(axis=1); k[~m.any(axis=1)]=H; return k
hasil=[]
for tk,g in d.groupby('ticker',sort=False):
    g=g.reset_index(drop=True); T=len(g)
    if T<252+H+5: continue
    o_,h_,l_,c_,v_=g.open,g.high,g.low,g.close,g.volume
    pc=c_.shift(); tr=pd.concat([h_-l_,(h_-pc).abs(),(l_-pc).abs()],axis=1).max(axis=1)
    atr14=wilder(tr,14); atr20=tr.rolling(20).mean()
    dl=c_.diff(); rsi=100-100/(1+wilder(dl.clip(lower=0),14)/wilder((-dl).clip(lower=0),14).replace(0,np.nan))
    ma10,ma20=c_.rolling(10).mean(),c_.rolling(20).mean(); ema20=c_.ewm(span=20,adjust=False,min_periods=20).mean()
    macd=c_.ewm(span=12,adjust=False).mean()-c_.ewm(span=26,adjust=False).mean(); sig=macd.ewm(span=9,adjust=False).mean()
    sd=c_.rolling(20).std(ddof=0)
    kc_atas=ema20+2*atr20                                   # Keltner (EMA20, 2xATR)
    sq_on=(ma20+2*sd<ma20+1.5*atr20)&(ma20-2*sd>ma20-1.5*atr20)   # TTM: BB dalam KC(1.5)
    mom=c_-((h_.rolling(20).max()+l_.rolling(20).min())/2+ma20)/2
    E={'MACD silang naik':silang(macd,sig),
       'MA10 silang atas MA20':silang(ma10,ma20),
       'Tutup pecah atas Keltner':silang(c_,kc_atas),
       'RSI14 silang atas 50':silang(rsi,pd.Series(50.0,index=g.index)),
       'Squeeze lepas ke atas':(~sq_on)&sq_on.shift().fillna(False)&(mom>0)}
    nama=list(E); ev5=pd.concat([dalam(E[n],5) for n in nama],axis=1); bil=ev5.sum(axis=1)
    hari_ini=pd.concat([E[n] for n in nama],axis=1).any(axis=1)
    S={'ASAS setiap bar':pd.Series(True,index=g.index)}
    S.update({'1 '+n:E[n] for n in nama})
    for a,b in itertools.combinations(range(5),2):
        S[f'2 {nama[a]} + {nama[b]} (5 hari)']=hari_ini&ev5.iloc[:,a]&ev5.iloc[:,b]
    S['3+ mana-mana 3 isyarat dalam 5 hari']=hari_ini&(bil>=3)
    S['4+ mana-mana 4 isyarat dalam 5 hari']=hari_ini&(bil>=4)
    S['5 kelima-lima dalam 5 hari']=hari_ini&(bil>=5)
    S['K keadaan: MACD>isyarat & MA10>MA20 & RSI 50-70 & tutup>EMA20 & squeeze lepas <=10 hari']=(macd>sig)&(ma10>ma20)&rsi.between(50,70)&(c_>ema20)&dalam(E['Squeeze lepas ke atas'],10)
    S['K2 keadaan tanpa squeeze: MACD>isyarat & MA10>MA20 & RSI 50-70 & tutup>EMA20']=(macd>sig)&(ma10>ma20)&rsi.between(50,70)&(c_>ema20)
    o,h,l,c=(g[k].to_numpy(float) for k in ('open','high','low','close'))
    e=np.arange(253,T-H-1); W=lambda a:swv(np.asarray(a,float),H)[e]
    O,L,C=W(o),W(l),W(c); NO=swv(o,H)[e+1]; P=o[e][:,None]; kk=np.arange(H)[None,:]
    cmax=np.maximum.accumulate(C,axis=1); chand=C<np.maximum.accumulate(cmax-4*W(atr14),axis=1)
    kosong=np.zeros_like(C,bool); h8=np.broadcast_to(P*(1-HENTI),C.shape)
    def laksana(sg,henti):
        sg=sg.copy(); sg[:,H-1]=True; ks=pertama(sg); t=4*ks+4; px=np.take_along_axis(NO,ks[:,None],1)[:,0]
        if henti is not None:
            kh=pertama(L<=henti); khc=np.minimum(kh,H-1)[:,None]
            pxh=np.minimum(np.take_along_axis(O,khc,1),np.take_along_axis(henti,khc,1))[:,0]
            th=np.where(kh<H,4*kh+1,10**9); m=th<t; t=np.where(m,th,t); px=np.where(m,pxh,px)
        return px/P[:,0]-1-KOS, t//4+1
    K={'henti -8% sahaja':(kosong,h8),'henti -8% + Chandelier 4x':(chand,h8),'Chandelier 4x tanpa henti':(chand,None),
       'henti -8% + MACD silang turun':(W(macd)<W(sig),h8),'henti -8% + MA10 bawah MA20':(W(ma10)<W(ma20),h8),
       'henti -8% + pegang 20 hari':(np.broadcast_to(kk==19,C.shape),h8)}
    tar=g.date.to_numpy()[e-1]; ok=((c_*v_).rolling(20).mean().to_numpy()[e-1]>=1e5)
    for kn,(sg,ht) in K.items():
        r,hari=laksana(sg,ht)
        for sn,sv in S.items():
            m=sv.to_numpy(bool)[e-1]&ok
            if m.any(): hasil.append(pd.DataFrame({'masuk':sn,'keluar':kn,'thn':tar[m]//10000,'r':r[m],'hari':hari[m]}))
R=pd.concat(hasil,ignore_index=True); R['tempoh']=np.where(R.thn<2023,'A','B')
pd.set_option('display.width',260,'display.max_rows',500,'display.max_colwidth',95)
g=R.groupby(['masuk','keluar'])
T=pd.DataFrame({'n':g.size(),'jgk':g.r.mean()*100,'mng':g.r.apply(lambda s:(s>0).mean()*100),'hari':g.hari.mean()})
pt=R.groupby(['masuk','keluar','tempoh']).r.mean().mul(100).unstack()
py=R.groupby(['masuk','keluar','thn']).r.mean().mul(100).unstack()
for kn in R.keluar.unique():
    x=T.xs(kn,level='keluar').copy(); a=pt.xs(kn,level='keluar'); y=py.xs(kn,level='keluar')
    x['lift_A']=a['A']-a.loc['ASAS setiap bar','A']; x['lift_B']=a['B']-a.loc['ASAS setiap bar','B']
    ly=y-y.loc['ASAS setiap bar']; x['thn_lift_positif']=(ly>0).sum(axis=1).astype(str)+'/'+ly.notna().sum(axis=1).astype(str)
    print('\n==',kn); print(x.round(2).to_string())
