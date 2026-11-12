import pandas as pd, numpy as np, json
XN=json.load(open('panel_mentah.pkl.keluar.json'))
def dalam(m,N):
    cs=np.cumsum(m,axis=0,dtype=np.int32); o=cs.copy(); o[N:]-=cs[:-N]; return o>0
class S:
    def __init__(s,f):
        P=pd.read_pickle(f); s.dts=np.sort(P.tarikh.unique()); di=np.searchsorted(s.dts,P.tarikh.to_numpy()); ti=P.saham.cat.codes.to_numpy(); sh=(len(s.dts),len(P.saham.cat.categories))
        def M(v,fill,dt=float):
            m=np.full(sh,fill,dtype=dt); m[di,ti]=np.asarray(v,dt); return m
        s.layak=M(P.layak,False,bool); s.a50=M(P.f_ma50>0,False,bool); s.a200=M(P.f_ma200>0,False,bool)
        s.X={k:M(P[f'x{XN.index(k):02d}']*100,np.nan) for k in ['dua tutup bawah MA50','TANPA henti: dua tutup bawah MA50','TANPA henti: Chandelier 4xATR']}
        s.D=M(P[f'd{XN.index("TANPA henti: dua tutup bawah MA50"):02d}'],np.nan); s.mae=M(P.mae20*100,np.nan)
        s.YR=np.broadcast_to((s.dts//10000)[:,None],sh); s.E={k:M(P[k],False,bool) for k in P.columns if k[:2]=='e_'}
        s.rsi2=M(P['A09 RSI2<10 atas MA200 (Connors)'],False,bool)
    def lap(s,m,k):
        m=m&s.layak; x=s.X[k][m]; g=~np.isnan(x); x=x[g]; y=s.YR[m][g]
        if len(x)==0: return dict(n=0)
        yy=pd.Series(x).groupby(y).mean()
        return dict(n=len(x),jgk=round(x.mean(),2),med=round(float(np.median(x)),2),mng=round((x>0).mean()*100,1),pmng=round(x[x>0].mean(),1),prugi=round(x[x<=0].mean(),1),hari=round(float(np.nanmean(s.D[m])),1),A=round(x[y<2023].mean(),2) if (y<2023).any() else None,B=round(x[y>=2023].mean(),2),thn=[round(float(v),1) for v in yy.values],p1=round(float(np.percentile(x,1)),1),p5=round(float(np.percentile(x,5)),1),lebih15=round((x<-15).mean()*100,1))
P=S('panel_mentah.pkl'); V=S('panel_stor.pkl')
DEF={'N201X36 MA20 silang atas MA50 (tutup>MA50)':lambda s:s.E['e_ma2050']&s.a50,
     'N202X36 RSI2<10 & tutup>MA200 & tutup>MA50':lambda s:s.rsi2&s.a50,
     'N203X36 gap naik 2% (10h) -> MA20 silang MA50 (tutup>MA50)':lambda s:s.E['e_ma2050']&dalam(s.E['e_gap'],10)&s.a50,
     'N204X36 RSI2<10 -> gap 2% (5h) -> RSI14 silang 50 (5h) (tutup>MA50)':lambda s:s.E['e_rsi50']&dalam(s.E['e_gap']&dalam(s.E['e_rsi2'],5),5)&s.a50,
     'rujukan N06X36 golden cross (tanpa syarat MA50)':lambda s:s.E['e_gc'],
     'rujukan N76X36 mana-mana hari tutup>MA50':lambda s:s.a50}
out={}
for nm,fn in DEF.items():
    out[nm]={}
    for k in ['TANPA henti: dua tutup bawah MA50','dua tutup bawah MA50','TANPA henti: Chandelier 4xATR']:
        a=P.lap(fn(P),k); b=V.lap(fn(V),k); out[nm][k]=dict(utama=a,lain={q:b.get(q) for q in ('n','jgk','mng')})
        print(nm,'|',k); print('   utama',a); print('   lain ',out[nm][k]['lain'])
json.dump(out,open('pradaftar.json','w'),ensure_ascii=False,indent=1)
