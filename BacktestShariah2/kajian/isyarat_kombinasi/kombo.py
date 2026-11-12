import pandas as pd, numpy as np, json, itertools
pd.set_option('display.width',330,'display.max_rows',400,'display.max_colwidth',95)
XN=json.load(open('panel_mentah.pkl.keluar.json')); j=XN.index('dua tutup bawah MA50')
def muat(f):
    P=pd.read_pickle(f); P['thn']=P.tarikh//10000
    lj=(P.f_pos>=0.75)
    P['D01 Saham tidur melonjak (ADX<25, Bollinger sempit, naik>=4%, volum 1.5x)']=lj&(P.f_ret1>=0.04)&(P.f_vr>=1.5)&(P.f_adx1<25)&(P.f_bbwp<=0.5)
    P['D02 Saham tidur melonjak kuat (ADX<20, Bollinger 30% bawah, naik>=6%)']=lj&(P.f_ret1>=0.06)&(P.f_vr>=1.5)&(P.f_adx1<20)&(P.f_bbwp<=0.3)
    SIG=[c for c in P.columns if c[:1] in 'ABCD' and c[1:3].isdigit()]
    # isyarat dalam 5 hari terakhir (ikut saham; baris tersusun ikut tarikh dalam setiap saham)
    W=P.groupby('saham',observed=True)[SIG].transform(lambda s:s.astype(float).rolling(5,min_periods=1).max()).astype(bool)
    return P,SIG,W
P,SIG,W=muat('panel_mentah.pkl'); V,_,WV=muat('panel_stor.pkl')
r=P[f'x{j:02d}'].to_numpy()*100; rv=V[f'x{j:02d}'].to_numpy()*100; hari=P[f'd{j:02d}'].to_numpy()
thn=P.thn.to_numpy(); atas=(P.layak&(P.f_ma50>0)).to_numpy(); atasV=(V.layak&(V.f_ma50>0)).to_numpy()
def lap(nm,m,mv):
    x=r[m]; 
    if len(x)<50: return None
    t=thn[m]; yy=pd.Series(x).groupby(t).agg(['mean','size']); yy=yy[yy['size']>=15]; xv=rv[mv]
    return dict(isyarat=nm,n=len(x),jgk=x.mean(),mng=(x>0).mean()*100,pmng=x[x>0].mean(),prugi=x[x<=0].mean(),hari=hari[m].mean(),A=x[t<2023].mean(),B=x[t>=2023].mean(),thn_untung=f"{(yy['mean']>0).sum()}/{len(yy)}",terburuk=yy['mean'].min(),nV=len(xv),jgkV=xv.mean() if len(xv) else np.nan,mngV=(xv>0).mean()*100 if len(xv) else np.nan)
c=['isyarat','n','jgk','mng','pmng','prugi','hari','A','B','thn_untung','terburuk','nV','jgkV','mngV']
k=lap('KAWALAN: mana-mana hari atas MA50',atas,atasV); print(pd.DataFrame([k])[c].round(2).to_string(index=False))
# 1. semua 47 isyarat tunggal
R=[lap(s,atas&P[s].to_numpy(),atasV&V[s].to_numpy()) for s in SIG]; T1=pd.DataFrame([x for x in R if x])
print('\n== 1. SEMUA isyarat tunggal (saham atas MA50; henti -8% + dua tutup bawah MA50) =='); print(T1.sort_values('jgk',ascending=False)[c].round(2).to_string(index=False))
# 2. tapis konteks
K={'RS>=80':(P.rs>=80).to_numpy(),'atas MA200':(P.f_ma200>0).to_numpy(),'QQQ ON':P.on.to_numpy(),'QQQ OFF':(~P.on).to_numpy(),'dalam 10% dari puncak 52w':(P.f_j52>=-0.10).to_numpy(),'30%+ bawah puncak 52w':(P.f_j52<=-0.30).to_numpy(),'volum >=1.5x':(P.f_vr>=1.5).to_numpy(),'ADX semalam <20':(P.f_adx1<20).to_numpy(),'ADX semalam >=30':(P.f_adx1>=30).to_numpy(),'0-5% atas MA50':((P.f_ma50>0)&(P.f_ma50<0.05)).to_numpy(),'>10% atas MA50':(P.f_ma50>0.10).to_numpy()}
KV={'RS>=80':(V.rs>=80).to_numpy(),'atas MA200':(V.f_ma200>0).to_numpy(),'QQQ ON':V.on.to_numpy(),'QQQ OFF':(~V.on).to_numpy(),'dalam 10% dari puncak 52w':(V.f_j52>=-0.10).to_numpy(),'30%+ bawah puncak 52w':(V.f_j52<=-0.30).to_numpy(),'volum >=1.5x':(V.f_vr>=1.5).to_numpy(),'ADX semalam <20':(V.f_adx1<20).to_numpy(),'ADX semalam >=30':(V.f_adx1>=30).to_numpy(),'0-5% atas MA50':((V.f_ma50>0)&(V.f_ma50<0.05)).to_numpy(),'>10% atas MA50':(V.f_ma50>0.10).to_numpy()}
R=[lap('KAWALAN + '+kn,atas&K[kn],atasV&KV[kn]) for kn in K]
print('\n== 2. KONTEKS sahaja (mana-mana hari atas MA50 + syarat) =='); print(pd.DataFrame(R)[c].round(2).to_string(index=False))
# 3. pasangan: isyarat X hari ini + isyarat Y dalam 5 hari
Sm={s:P[s].to_numpy() for s in SIG}; Wm={s:W[s].to_numpy() for s in SIG}; SmV={s:V[s].to_numpy() for s in SIG}; WmV={s:WV[s].to_numpy() for s in SIG}
R=[]
for a,b in itertools.combinations(SIG,2):
    m=atas&((Sm[a]&Wm[b])|(Sm[b]&Wm[a])); mv=atasV&((SmV[a]&WmV[b])|(SmV[b]&WmV[a]))
    x=lap(a[:3]+'+'+b[:3]+' | '+a[4:38]+' + '+b[4:38],m,mv)
    if x: R.append(x)
T3=pd.DataFrame(R); T3.to_pickle('kombo_pasangan.pkl')
print('\n== 3. PASANGAN: bil diuji',len(T3),'| purata jgk',round(T3.jgk.mean(),2),'| median',round(T3.jgk.median(),2),'| bahagian lebih baik drpd kawalan 1.36:',round((T3.jgk>1.36).mean()*100),'%')
ok=T3[(T3.n>=300)&(T3.A>0)&(T3.B>0)&(T3.thn_untung.str[0].astype(int)>=6)]
print('lulus tapis (n>=300, untung dua separuh, >=6 tahun untung):',len(ok))
print(ok.sort_values('jgk',ascending=False)[c].head(20).round(2).to_string(index=False))
ok2=ok[(ok.nV>=30)]
print('\nantara yang lulus & ada >=30 isyarat pada saham lain:',len(ok2),'| purata jgk set utama',round(ok2.jgk.mean(),2),'| purata jgk saham lain',round(ok2.jgkV.mean(),2),'| korelasi',round(ok2.jgk.corr(ok2.jgkV),2),'| bahagian positif pd saham lain',round((ok2.jgkV>0).mean()*100),'%')
t20=ok2.sort_values('jgk',ascending=False).head(20); print('20 teratas: set utama',round(t20.jgk.mean(),2),'-> saham lain',round(t20.jgkV.mean(),2),'| positif',int((t20.jgkV>0).sum()),'/20')
ok3=ok2[(ok2.jgkV>1.0)&(ok2.jgk>2.0)]; print('\n-- pasangan yang >2% set utama DAN >1% saham lain --',len(ok3)); print(ok3.sort_values('jgk',ascending=False)[c].head(15).round(2).to_string(index=False))
# 4. bilangan isyarat sepakat dalam 5 hari (17 isyarat peristiwa A)
EV=[s for s in SIG if s[0]=='A' and s not in ('A09 RSI2<10 atas MA200 (Connors)','A12 Bawah jalur bawah Bollinger + RSI<30','A08 RSI14 silang atas 30 (bangkit terlebih jual)')]
bil=sum(Wm[s].astype(int) for s in EV); hi=np.any([Sm[s] for s in EV],axis=0); bilV=sum(WmV[s].astype(int) for s in EV); hiV=np.any([SmV[s] for s in EV],axis=0)
R=[lap(f'{lo}-{hi_} isyarat indikator sepakat (5 hari)',atas&hi&(bil>=lo)&(bil<=hi_),atasV&hiV&(bilV>=lo)&(bilV<=hi_)) for lo,hi_ in ((1,1),(2,2),(3,4),(5,6),(7,17))]
print('\n== 4. BILANGAN isyarat indikator sepakat =='); print(pd.DataFrame([x for x in R if x])[c].round(2).to_string(index=False))
