from pathlib import Path
from oraculo import ROOT, ORACLE, MATERIAL, LOG, run
import random, json, subprocess, os, re, sys, time

EXE = Path(os.environ.get('AF_SOLUTION', ROOT / ('pruebas/codigo1.exe' if os.name == 'nt' else 'pruebas/codigo1')))
RNG = random.Random(20261105)

def compare(data, name):
    expected = run(data)
    actual = run(data, EXE)
    if actual != expected:
        lines = data.split('\n')
        head, body = lines[0], lines[2:-1]
        # Reduce by deleting chunks, then individual lines; preserve the header.
        chunk = max(1,len(body)//2)
        while chunk:
            i = 0
            while i < len(body):
                trial = body[:i] + body[i+chunk:]
                text = head+'\n'+str(len(trial))+'\n'+'\n'.join(trial)+'\n'
                if run(text) != run(text,EXE): body=trial
                else: i += chunk
            chunk //= 2
        minimal = head+'\n'+str(len(body))+'\n'+'\n'.join(body)+'\n'
        (ROOT/'pruebas/discrepancia.in').write_text(minimal,encoding='utf-8')
        raise AssertionError((name,repr(minimal),repr(run(minimal)),repr(run(minimal,EXE))))

def main(count=3000):
    start=time.perf_counter()
    records=[json.loads(x) for x in LOG.read_text(encoding='utf-8').splitlines()]
    checked=0
    for r in records:
        if r['output'].startswith('ERROR:'): continue
        compare(r['input'],r['name']); checked+=1
    d=MATERIAL
    for i in (1,2): compare((d/f'ejemplo{i}.in').read_text(),f'ejemplo{i}')
    for k in range(count):
        n=RNG.randrange(1,301); t=RNG.randrange(0,10)
        lines=[]; prev={}
        lo=RNG.randrange(0,40); hi=RNG.randrange(lo,301)
        g=RNG.choice([0,1,2,10,20,50,1000000000])
        for _ in range(n):
            t+=RNG.randrange(0,4)
            u=RNG.choice([0,1,2,3,4,5,6,7,1999999,1999998])
            a=RNG.choice(['READ','WRITE','LOGIN','LOGOUT'])
            if RNG.random()<.25 and u in prev and prev[u][0]==t: a=prev[u][1]
            prev[u]=(t,a)
            ts=str(t); us=str(u)
            mode=RNG.randrange(20)
            if mode==0: ts='0'*RNG.randrange(1,15)+ts
            if mode==1: us='0'*RNG.randrange(1,15)+us
            if mode==2: ts=RNG.choice(['-1','1000000001','+0','0.0','1e2','99999999999999999999999'])
            if mode==3: us=RNG.choice(['-1','2000000','+1','1.0','0x1'])
            if mode==4: a=RNG.choice(['read','FOO','LOGINX',''])
            line=f'{ts} {us} {a}'
            if mode==5: line=RNG.choice(['',' ','0 1','0',' 0 1 READ','0  1 READ','0 1 READ x'])
            if mode==6: line=line.replace(' ',RNG.choice(['\t','  ','\v','\f']))
            if mode==7: line+=RNG.choice([' ','\t','\r','\r\r','\r\r\r','\x00'])
            lines.append(line)
        data=f'{lo} {hi} {g}\n{n}\n'+'\n'.join(lines)+'\n'
        compare(data,f'random_{k}')
        if (k+1)%250==0: print('Aleatorias',k+1,flush=True)
    result=dict(seed=20261105,regressions=checked,official=2,random=count,seconds=round(time.perf_counter()-start,3),comparison='byte for byte, native Windows CRLF')
    suffix='aleatorias' if count else 'regresiones'
    (ROOT/f'pruebas/diferencial_{suffix}_resultado.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(result)

if __name__=='__main__': main(int(sys.argv[1]) if len(sys.argv)>1 else 3000)
