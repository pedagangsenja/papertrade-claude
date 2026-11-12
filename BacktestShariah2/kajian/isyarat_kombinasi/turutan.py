import pandas as pd, numpy as np, itertools, time
pd.set_option('display.width',330,'display.max_rows',400,'display.max_colwidth',110)
NAMA={'k_macd':'MACD hijau (MACD>isyarat)','k_macd0':'MACD atas sifar','k_ma1020':'MA10>MA20','k_ma2050':'MA20>MA50','k_ma50200':'MA50>MA200','k_c200':'tutup>MA200','k_rsi50':'RSI>50','k_sqon':'squeeze ON','k_sqlepas10':'squeeze lepas (10 hari)','k_adx':'ADX>25 & +DI>-DI','k_st':'Supertrend naik','k_awan':'atas awan Ichimoku','k_ema20':'tutup>EMA20','k_stoch':'Stochastic %K>%D','k_vol':'volum>=1.5x','k_rs80':'RS>=80','k_52w':'dalam 10% puncak 52w',
 'e_macd':'MACD silang naik','e_sqon':'squeeze mula ON','e_sqlepas':'squeeze lepas ke atas','e_ma1020':'MA10 silang MA20','e_ma2050':'MA20 silang MA50','e_gc':'golden cross','e_rsi50':'RSI silang 50','e_kelt':'pecah Keltner','e_st':'Supertrend naik','e_awan':'pecah awan Ichimoku','e_hh20':'pecah tinggi 20 hari','e_adx':'ADX silang 25','e_rsi2':'undur RSI2<10','e_vol':'lonjakan 4% + volum 2x','e_c50':'tutup silang atas MA50'}
class Set:
    def __init__(s,f):
        P=pd.read_pickle(f); P['k_rs80']=P.rs>=80; P['k_52w']=P.f_j52>=-0.10
        s.dts=np.sort(P.tarikh.unique()); s.di=np.searchsorted(s.dts,P.tarikh.to_numpy()); s.ti=P.saham.cat.codes.to_numpy(); s.nt=len(P.saham.cat.categories)
        s.ok=s.M(P.layak&(P.f_ma50>0),False).astype(bool); s.R=s.M(P.x03*100,np.nan); s.ada=s.M(np.ones(len(P)),0)>0
        s.YR=np.broadcast_to((s.dts//10000)[:,None],s.R.shape)
        s.awal=np.zeros_like(s.ok); a=s.ada.argmax(axis=0); s.awal[a,np.arange(s.nt)]=True
        s.K={k:s.M(P[k],False).astype(bool) for k in P.columns if k[:2]=='k_'}; s.E={k:s.M(P[k],False).astype(bool) for k in P.columns if k[:2]=='e_'}
    def M(s,v,fill):
        m=np.full((len(s.dts),s.nt),fill,dtype=float); m[s.di,s.ti]=np.asarray(v,float); return m
    def mula(s,m):   # hari pertama m benar (semalam tidak)
        p=np.zeros_like(m); p[1:]=m[:-1]; return m&~p&~s.awal
    def stat(s,m):
        m=m&s.ok; x=s.R[m]; g=~np.isnan(x); x=x[g]
        if len(x)==0: return (0,np.nan,np.nan,np.nan,np.nan,0,0,0,0)
        y=s.YR[m][g]; a=x[y<2023]; b=x[y>=2023]
        cnt=np.bincount(y-2020,minlength=8); sm=np.bincount(y-2020,weights=x,minlength=8); v=cnt>=15
        return (len(x),x.mean(),(x>0).mean()*100,a.mean() if len(a) else np.nan,b.mean() if len(b) else np.nan,len(a),len(b),int(((sm[v]/cnt[v])>0).sum()),int(v.sum()))
def dalam(m,N):
    cs=np.cumsum(m,axis=0); o=cs.copy(); o[N:]-=cs[:-N]; return o>0
P=Set('panel_mentah.pkl'); V=Set('panel_stor.pkl')
allT=np.ones_like(P.ok); allTV=np.ones_like(V.ok)
kw=P.stat(allT); kv=V.stat(allTV); CA,CB,CV=kw[3],kw[4],kv[1]
print('KAWALAN (mana-mana hari atas MA50): semua %.2f | A %.2f | B %.2f | saham lain %.2f'%(kw[1],CA,CB,CV))
col=['nama','n','jgk','mng','A','B','nA','nB','thn_untung','thn','nV','jgkV']
def baris(nm,m,mv):
    a=P.stat(m); b=V.stat(mv); return dict(nama=nm,n=a[0],jgk=a[1],mng=a[2],A=a[3],B=a[4],nA=a[5],nB=a[6],thn_untung=a[7],thn=a[8],nV=b[0],jgkV=b[1])
def ujian(T,tajuk):
    T=T[(T.nA>=100)&(T.nB>=100)].copy(); T['xA']=T.A-CA; T['xB']=T.B-CB
    print(f'\n### {tajuk}: {len(T)} gabungan dengan >=100 dagangan setiap separuh')
    print('  purata untung %.2f | median %.2f | bahagian lebih baik drpd kawalan (kedua-dua separuh): %.0f%%'%(T.jgk.mean(),T.jgk.median(),((T.xA>0)&(T.xB>0)).mean()*100))
    print('  korelasi pangkat separuh A lawan separuh B (lebihan atas kawalan): %.2f'%T.xA.corr(T.xB,method='spearman'))
    tA=T.sort_values('xA',ascending=False).head(20); tB=T.sort_values('xB',ascending=False).head(20)
    print('  20 terbaik dipilih pada 2020-22: lebihan di sana %+.2f -> lebihan pada 2023-26 %+.2f (positif %d/20)'%(tA.xA.mean(),tA.xB.mean(),(tA.xB>0).sum()))
    print('  20 terbaik dipilih pada 2023-26: lebihan di sana %+.2f -> lebihan pada 2020-22 %+.2f (positif %d/20)'%(tB.xB.mean(),tB.xA.mean(),(tB.xA>0).sum()))
    ok=T[(T.n>=300)&(T.xA>0.3)&(T.xB>0.3)&(T.thn_untung>=T.thn-1)]
    okv=ok[(ok.nV>=30)]
    print('  lulus tapis (n>=300, lebihan >0.3 kedua-dua separuh, untung >=6/7 tahun): %d | drpdnya ada >=30 isyarat pada saham lain: %d, purata lebihan di sana %+.2f, positif %.0f%%'%(len(ok),len(okv),(okv.jgkV-CV).mean() if len(okv) else np.nan,((okv.jgkV-CV)>0).mean()*100 if len(okv) else np.nan))
    f=okv[okv.jgkV>CV+0.3].copy(); f['min_lebih']=f[['xA','xB']].min(axis=1)
    print('  -- lulus SEMUA (termasuk saham lain):',len(f)); 
    if len(f): print(f.sort_values('min_lebih',ascending=False)[col].head(8).round(2).to_string(index=False))
    return T
# ---------- 1. bilangan lampu hijau serentak ----------
ASAL17=['k_macd','k_macd0','k_ma1020','k_ma2050','k_ma50200','k_c200','k_rsi50','k_sqon','k_sqlepas10','k_adx','k_st','k_awan','k_ema20','k_stoch','k_vol','k_rs80','k_52w']
ASAL15=['e_macd','e_sqon','e_sqlepas','e_ma1020','e_ma2050','e_gc','e_rsi50','e_kelt','e_st','e_awan','e_hh20','e_adx','e_rsi2','e_vol','e_c50']
KS=ASAL17; print('\n== 1. BILANGAN keadaan hijau serentak (daripada',len(KS),') — beli pada hari pertama bilangan mencapai paras ==')
cnt=sum(P.K[k].astype(int) for k in KS); cntV=sum(V.K[k].astype(int) for k in KS)
R=[baris(f'tepat {a}-{b} hijau (mana-mana hari)',(cnt>=a)&(cnt<=b),(cntV>=a)&(cntV<=b)) for a,b in ((0,5),(6,8),(9,10),(11,12),(13,14),(15,17))]
R+=[baris(f'hari pertama mencapai >={k} hijau',P.mula(cnt>=k),V.mula(cntV>=k)) for k in (8,10,11,12,13,14,15)]
print(pd.DataFrame(R)[col].round(2).to_string(index=False))
# ---------- 2. set 4, 5, 6 keadaan serentak ----------
t0=time.time(); R=[]
for r_ in (4,5,6):
    for cb in itertools.combinations(KS,r_):
        m=P.K[cb[0]]
        for k in cb[1:]: m=m&P.K[k]
        a=P.stat(P.mula(m))
        if a[5]<100 or a[6]<100: continue
        mv=V.K[cb[0]]
        for k in cb[1:]: mv=mv&V.K[k]
        b=V.stat(V.mula(mv))
        R.append(dict(nama=' + '.join(NAMA[k] for k in cb),bil=r_,n=a[0],jgk=a[1],mng=a[2],A=a[3],B=a[4],nA=a[5],nB=a[6],thn_untung=a[7],thn=a[8],nV=b[0],jgkV=b[1]))
T2=pd.DataFrame(R); T2.to_pickle('serentak.pkl'); print('\n(masa %.0fs)'%(time.time()-t0))
for r_ in (4,5,6): ujian(T2[T2.bil==r_],f'2. SERENTAK {r_} keadaan (beli hari pertama semua hijau)')
# ---------- 3. berturutan ----------
N=10; ES=ASAL15; WP={k:dalam(P.E[k],N) for k in ES}; WVv={k:dalam(V.E[k],N) for k in ES}
t0=time.time(); R=[]; AB={}; ABv={}
for a,b in itertools.permutations(ES,2):
    m=P.E[b]&WP[a]; mv=V.E[b]&WVv[a]; AB[(a,b)]=dalam(m,N); ABv[(a,b)]=dalam(mv,N)
    s=P.stat(m); sv=V.stat(mv)
    R.append(dict(nama=f'{NAMA[a]} -> {NAMA[b]}',bil=2,kunci=(a,b),n=s[0],jgk=s[1],mng=s[2],A=s[3],B=s[4],nA=s[5],nB=s[6],thn_untung=s[7],thn=s[8],nV=sv[0],jgkV=sv[1]))
for a,b,c in itertools.permutations(ES,3):
    m=P.E[c]&AB[(a,b)]; s=P.stat(m)
    if s[5]<50 or s[6]<50: continue
    sv=V.stat(V.E[c]&ABv[(a,b)])
    R.append(dict(nama=f'{NAMA[a]} -> {NAMA[b]} -> {NAMA[c]}',bil=3,kunci=(a,b,c),n=s[0],jgk=s[1],mng=s[2],A=s[3],B=s[4],nA=s[5],nB=s[6],thn_untung=s[7],thn=s[8],nV=sv[0],jgkV=sv[1]))
T3=pd.DataFrame(R); T3.to_pickle('turutan.pkl'); print('\n(masa %.0fs)'%(time.time()-t0))
for r_ in (2,3): ujian(T3[T3.bil==r_],f'3. BERTURUTAN {r_} langkah (setiap langkah dalam {N} hari selepas langkah sebelumnya; beli pada langkah terakhir)')
# adakah SUSUNAN penting? banding susunan berbeza bagi set tiga peristiwa yang sama
t=T3[(T3.bil==3)&(T3.nA>=100)&(T3.nB>=100)].copy(); t['set']=t.kunci.apply(lambda k:tuple(sorted(k)))
t['dA']=t.A-t.groupby('set').A.transform('mean'); t['dB']=t.B-t.groupby('set').B.transform('mean'); t=t[t.groupby('set').A.transform('size')>=3]
print('\n  ADAKAH SUSUNAN PENTING? %d turutan dalam %d set. Korelasi pangkat (kesan susunan 2020-22 lawan 2023-26): %.2f'%(len(t),t.set.nunique(),t.dA.corr(t.dB,method='spearman')))
# contoh pengguna
for kunci,nm in [(('e_macd','e_sqon','e_ma1020'),'CONTOH ANDA: MACD silang naik -> squeeze mula ON -> MA10 silang MA20'),(('e_sqon','e_macd','e_ma1020'),'squeeze mula ON -> MACD silang naik -> MA10 silang MA20'),(('e_sqon','e_sqlepas','e_ma1020'),'squeeze mula ON -> squeeze lepas -> MA10 silang MA20')]:
    a,b,c=kunci; m=P.E[c]&AB[(a,b)]; mv=V.E[c]&ABv[(a,b)]; print(pd.DataFrame([baris(nm,m,mv)])[col].round(2).to_string(index=False,header=False))
m=P.E['e_ma1020']&P.K['k_macd']&dalam(P.K['k_sqon'],N); mv=V.E['e_ma1020']&V.K['k_macd']&dalam(V.K['k_sqon'],N)
print(pd.DataFrame([baris('versi longgar: MA10 silang MA20 semasa MACD hijau dan squeeze ON dalam 10 hari',m,mv)])[col].round(2).to_string(index=False,header=False))
