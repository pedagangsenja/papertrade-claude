import pandas as pd, numpy as np, sys
R=pd.read_pickle(sys.argv[1])
def ring(z):
    w,k=z.r[z.r>0],z.r[z.r<=0]
    return pd.Series({'n':len(z),'jgk':z.r.mean()*100,'mng':(z.r>0).mean()*100,'pmng':w.mean()*100,'prugi':k.mean()*100,'hari':z.hari.mean(),'pct_hari':z.r.mean()*100/z.hari.mean(),'henti':z.henti.mean()*100})
a=R[R.masuk=='ASAS setiap bar']
t=a.groupby('keluar')[['r','hari','henti']].apply(ring)
for nm,col in [('A',a.tempoh=='A 2020-22'),('B',a.tempoh!='A 2020-22'),('ON',a.on),('OFF',~a.on)]:
    z=a[col].groupby('keluar').agg(r=('r','mean'),h=('hari','mean'))
    t['jgk_'+nm]=z.r*100; t['ph_'+nm]=z.r*100/z.h
print(t.sort_values('pct_hari',ascending=False).round(3).to_string())
print()
g=R.groupby(['masuk','keluar','tempoh']).agg(r=('r','mean'),h=('hari','mean'),n=('r','size'))
g['ph']=g.r*100/g.h; g['r']*=100
for kn in ['pegang 126 hari (rujukan)','henti sahaja','henti + Chandelier 4xATR','Chandelier 4xATR TANPA henti (lorong 2 kini)','henti + dua tutup bawah MA50','henti + RSI14>70','henti + masa 20 hari']:
    x=g.xs(kn,level='keluar').unstack('tempoh')
    b=x.loc['ASAS setiap bar']
    out=pd.DataFrame({'n':x['n'].sum(axis=1),'jgk_A':x[('r','A 2020-22')],'jgk_B':x[('r','B 2023-26')],'lift_A':x[('r','A 2020-22')]-b[('r','A 2020-22')],'lift_B':x[('r','B 2023-26')]-b[('r','B 2023-26')],'ph_A':x[('ph','A 2020-22')],'ph_B':x[('ph','B 2023-26')]})
    print('--',kn); print(out.round(3).to_string())
