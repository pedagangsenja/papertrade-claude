import pandas as pd, numpy as np, itertools
P=pd.read_pickle('panel_mentah.pkl'); P=P[P.layak].reset_index(drop=True)
P['thn']=P.tarikh//10000
P['terc']=P.groupby('tarikh').atrp.transform(lambda s: pd.qcut(s.rank(method='first'),3,labels=False))
def baki(v): return v-v.groupby([P.tarikh,P.terc]).transform('mean')
for n in (5,10,20,40,60): P[f'e{n}']=baki(P[f'r{n}']*100); P[f'u{n}']=(P[f'r{n}']>0)*100.0; P[f'eu{n}']=baki(P[f'u{n}'])
P['em16']=baki(P.m16*100.0); P['em8']=baki(P.m8*100.0); P['ech']=baki(P.x01*100); P['elari']=baki(P.x00*100); P['ema50']=baki(P.x03*100)
P['r20w']=P.r20.clip(upper=0.5)*100; P['e20w']=baki(P.r20w)
def lap(m,nm):
    z=P[m]; yy=z.groupby('thn').e20.agg(['mean','size']); yy=yy[yy['size']>=10]
    return dict(isyarat=nm,n=len(z),saham=z.saham.nunique(),u20=z.u20.mean(),r20=z.r20.mean()*100,med20=z.r20.median()*100,
      L5=z.e5.mean(),L10=z.e10.mean(),L20=z.e20.mean(),L20w=z.e20w.mean(),L40=z.e40.mean(),L60=z.e60.mean(),Lu20=z.eu20.mean(),
      A=z.e20[z.thn<2023].mean(),B=z.e20[z.thn>=2023].mean(),thn=f"{(yy['mean']>0).sum()}/{len(yy)}",Lm8=z.em8.mean(),Lm16=z.em16.mean(),Lch=z.ech.mean(),Llari=z.elari.mean(),Lma50=z.ema50.mean())
pd.set_option('display.width',330,'display.max_rows',300,'display.max_colwidth',60)
print('== GRID keteguhan: lonjakan + volum + tutup dekat tinggi, dengan/tanpa "tidur" ==')
R=[]
for nk,v_,ad,bw in itertools.product((0.03,0.04,0.06),(1.5,2,3),(None,20,25),(None,0.3,0.5)):
    m=(P.f_ret1>=nk)&(P.f_vr>=v_)&(P.f_pos>=0.75)
    if ad: m&=(P.f_adx1<ad)
    if bw: m&=(P.f_bbwp<=bw)
    R.append(lap(m,f'naik>={nk:.0%} vol>={v_}x adx<{ad} bbw<={bw}'))
G=pd.DataFrame(R).set_index('isyarat'); print(G.round(2).to_string())
print('\nringkas grid: tanpa tidur L20 purata',G[G.index.str.contains('adx<None bbw<=None')].L20.mean().round(2),'| dengan adx & bbw',G[~G.index.str.contains('None')].L20.mean().round(2),'| bil positif',(G[~G.index.str.contains('None')].L20>0).sum(),'/',len(G[~G.index.str.contains('None')]))
print('\n== TIDUR sahaja (tanpa lonjakan) dan lonjakan tanpa volum ==')
R=[lap((P.f_adx1<20)&(P.f_bbwp<=0.3),'tidur sahaja (adx<20 & bbw<=30%)'),
   lap((P.f_adx1<20)&(P.f_bbwp<=0.3)&(P.f_ret1>=0.04),'tidur + naik>=4% (tanpa syarat volum)'),
   lap((P.f_adx1<20)&(P.f_bbwp<=0.3)&(P.f_vr>=2)&(P.f_ret1>0),'tidur + volum 2x + hari naik (tanpa syarat 4%)'),
   lap((P.f_adx1<20)&(P.f_bbwp<=0.3)&(P.f_vr>=2)&(P.f_ret1<=-0.04),'tidur + volum 2x + JATUH >=4% (songsang)'),
   lap((P.f_adx1>=30)&(P.f_ret1>=0.04)&(P.f_vr>=2)&(P.f_pos>=0.75),'lonjakan bila sudah trending (adx>=30)'),
   lap((P.f_ret1>=0.04)&(P.f_vr>=2)&(P.f_pos>=0.75)&(P.f_adx1<20)&(P.f_bbwp<=0.3)&(P.f_ma200>0),'B05 + atas MA200'),
   lap((P.f_ret1>=0.04)&(P.f_vr>=2)&(P.f_pos>=0.75)&(P.f_adx1<20)&(P.f_bbwp<=0.3)&(P.f_ma200<=0),'B05 + bawah MA200'),
   lap((P.f_ret1>=0.04)&(P.f_vr>=2)&(P.f_pos>=0.75)&(P.f_adx1<20)&(P.f_bbwp<=0.3)&P.on,'B05 + rejim QQQ ON'),
   lap((P.f_ret1>=0.04)&(P.f_vr>=2)&(P.f_pos>=0.75)&(P.f_adx1<20)&(P.f_bbwp<=0.3)&~P.on,'B05 + rejim QQQ OFF'),
   lap((P.f_ret1>=0.04)&(P.f_vr>=2)&(P.f_pos>=0.75)&(P.f_adx1<20)&(P.f_bbwp<=0.3)&(P.f_gap>=0.03),'B05 + gap >=3%'),
   lap((P.f_ret1>=0.04)&(P.f_vr>=2)&(P.f_pos>=0.75)&(P.f_adx1<20)&(P.f_bbwp<=0.3)&(P.f_gap<0.03),'B05 + tanpa gap'),
   lap(P['A06 Golden cross MA50/MA200'],'A06 golden cross'),
   lap(P['C04 RS >=90 & atas MA50 (keadaan)'],'C04 RS>=90 & atas MA50'),
   lap(P['A09 RSI2<10 atas MA200 (Connors)'],'A09 RSI2<10 atas MA200'),
   lap(P.on,'semua saham, rejim ON'),lap(~P.on,'semua saham, rejim OFF')]
print(pd.DataFrame(R).set_index('isyarat').round(2).to_string())
print('\nrejim: r20 mentah ON',round(P.r20[P.on].mean()*100,2),'OFF',round(P.r20[~P.on].mean()*100,2),'| u20 ON',round(P.u20[P.on].mean(),1),'OFF',round(P.u20[~P.on].mean(),1),'| m16 ON',round(P.m16[P.on].mean()*100,1),'OFF',round(P.m16[~P.on].mean()*100,1),'| kena8 ON',round(P.kena8[P.on].mean()*100,1),'OFF',round(P.kena8[~P.on].mean()*100,1))
# B05 ikut tahun
m=(P.f_ret1>=0.04)&(P.f_vr>=2)&(P.f_pos>=0.75)&(P.f_adx1<20)&(P.f_bbwp<=0.3)
print('\nB05 ikut tahun:'); print(P[m].groupby('thn').agg(n=('r20','size'),saham=('saham','nunique'),u20=('u20','mean'),r20=('r20',lambda s:s.mean()*100),med=('r20',lambda s:s.median()*100),L20=('e20','mean'),Lm16=('em16','mean'),Lch=('ech','mean')).round(2).to_string())
