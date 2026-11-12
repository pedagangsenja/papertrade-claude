import pandas as pd, numpy as np, json, sys
rng=np.random.default_rng(7)
P=pd.read_pickle('panel_mentah.pkl'); P=P[P.layak].reset_index(drop=True)
SIG=[c for c in P.columns if c[:1] in 'ABC' and c[1:3].isdigit()]
P['thn']=P.tarikh//10000; P['bln']=P.tarikh//100
P['terc']=P.groupby('tarikh').atrp.transform(lambda s: pd.qcut(s.rank(method='first'),3,labels=False))
Y={'u20':(P.r20>0).astype(float)*100,'r20':P.r20*100,'u5':(P.r5>0).astype(float)*100,'u10':(P.r10>0).astype(float)*100,'u40':(P.r40>0).astype(float)*100,
   'r40':P.r40*100,'m8':P.m8.astype(float)*100,'m16':P.m16.astype(float)*100,'m24':P.m24.astype(float)*100,'kena8':P.kena8.astype(float)*100,
   'mae20':P.mae20*100,'xch':P.x01*100,'xlari':P.x00*100,'xma50':P.x03*100}
for k,v in Y.items():
    P['y_'+k]=v
    P['e_'+k]=v-v.groupby([P.tarikh,P.terc]).transform('mean')          # baki: tolak purata hari x tercile ATR
    P['w_'+k]=P['e_'+k]-P['e_'+k].groupby(P.saham,observed=True).transform('mean')  # tolak purata saham itu sendiri
# matriks untuk plasebo anjak-masa
dts=np.sort(P.tarikh.unique()); tks=P.saham.cat.categories
di=np.searchsorted(dts,P.tarikh.to_numpy()); ti=P.saham.cat.codes.to_numpy()
def mat(col,fill=np.nan):
    M=np.full((len(dts),len(tks)),fill,dtype=float); M[di,ti]=P[col].to_numpy(dtype=float); return M
E_={k:mat('e_'+k) for k in ('r20','m16','xch')}
def plasebo(sn,k,n=400):
    S=mat(sn,0.0)>0; E=E_[k]; sebenar=np.nanmean(E[S]); T=len(dts); bil=0
    for _ in range(n):
        an=rng.integers(60,T-60,size=S.shape[1]); idx=(np.arange(T)[:,None]-an[None,:])%T
        Sp=np.take_along_axis(S,idx,axis=0)
        if np.nanmean(E[Sp])>=sebenar: bil+=1
    return (bil+1)/(n+1)
rows=[]
for sn in SIG:
    z=P[P[sn]]
    r={'isyarat':sn,'n':len(z)}
    for k in Y: r[k]=z['y_'+k].mean()
    for k in ('u20','r20','m8','m16','xch','xlari','xma50','r40'): r['L_'+k]=z['e_'+k].mean()
    for k in ('r20','m16','xch'):
        r['W_'+k]=z['w_'+k].mean()
        r['LA_'+k]=z.loc[z.thn<2023,'e_'+k].mean(); r['LB_'+k]=z.loc[z.thn>=2023,'e_'+k].mean()
        yy=z.groupby('thn')['e_'+k].agg(['mean','size']); yy=yy[yy['size']>=15]
        r['thn_'+k]=f"{(yy['mean']>0).sum()}/{len(yy)}"
        r['p_'+k]=plasebo(sn,k)
    rows.append(r)
T=pd.DataFrame(rows).set_index('isyarat')
T.to_pickle('hasil_isyarat.pkl')
asas={k:P['y_'+k].mean() for k in Y}
print('ASAS (semua saham layak, semua hari): n',len(P),{k:round(v,2) for k,v in asas.items()})
pd.set_option('display.width',330,'display.max_rows',200,'display.max_colwidth',52)
print('\n== HASIL MENTAH (%), disusun ikut lift r20 ==')
print(T.sort_values('L_r20',ascending=False)[['n','u5','u10','u20','u40','r20','m8','m16','m24','kena8','mae20','xch','xlari','xma50']].round(1).to_string())
print('\n== LIFT lawan hari sama x tercile ATR (mata) dan ujian ==')
c=['n','L_u20','L_r20','LA_r20','LB_r20','thn_r20','W_r20','p_r20','L_m16','LA_m16','LB_m16','thn_m16','W_m16','p_m16','L_xch','LA_xch','LB_xch','thn_xch','W_xch','p_xch']
print(T.sort_values('L_r20',ascending=False)[c].round(2).to_string())
