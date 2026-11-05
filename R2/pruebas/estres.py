"""Generate each 5M-line input, independently compute answers, measure Windows peak WS.
The oracle is deliberately never called here.
"""
from pathlib import Path
import ctypes, ctypes.wintypes as wt, subprocess, time, json, hashlib, os
from array import array
from oraculo import ROOT

N=5000000
EXE=ROOT/'pruebas/codigo1.exe'
INPUT=ROOT/'pruebas/estres.in'

class Counters(ctypes.Structure):
    _fields_=[('cb',wt.DWORD),('PageFaultCount',wt.DWORD)]+[(n,ctypes.c_size_t) for n in
        ('PeakWorkingSetSize','WorkingSetSize','QuotaPeakPagedPoolUsage','QuotaPagedPoolUsage',
         'QuotaPeakNonPagedPoolUsage','QuotaNonPagedPoolUsage','PagefileUsage','PeakPagefileUsage')]

get_memory=ctypes.WinDLL('psapi').GetProcessMemoryInfo
get_memory.argtypes=[wt.HANDLE,ctypes.POINTER(Counters),wt.DWORD]
get_memory.restype=wt.BOOL

def bench(expected):
    peak=commit=0
    with INPUT.open('rb') as f:
        start=time.perf_counter()
        p=subprocess.Popen([str(EXE)],stdin=f,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        while True:
            m=Counters();m.cb=ctypes.sizeof(m)
            if get_memory(wt.HANDLE(int(p._handle)),ctypes.byref(m),m.cb):
                peak=max(peak,m.PeakWorkingSetSize);commit=max(commit,m.PeakPagefileUsage)
            if p.poll() is not None: break
            time.sleep(.001)
        out,err=p.communicate()
        elapsed=time.perf_counter()-start
    actual=out.decode().replace('\r\n','\n')
    assert p.returncode==0 and not err,(p.returncode,err)
    assert actual==expected,(actual,expected)
    assert peak>0
    return dict(seconds=round(elapsed,4),peak_working_set_bytes=peak,
                peak_private_commit_bytes=commit,output=actual)

def generate(kind):
    counts=array('I',[0])*2000000
    last=array('q',[-1])*2000000
    sums=array('q',[0])*2000000
    nums=array('I',[0])*2000000
    t1,t2,g=0,1000000000,1000000000
    if kind=='un_usuario': g=200
    if kind=='muchos_usuarios' or kind=='uniforme_permutado': g=1
    if kind=='dentro_fuera':t1,t2=1000000,3000000
    if kind=='sin_brechas':g=0
    if kind=='invalidos':g=200
    actions=['READ','WRITE','LOGIN','LOGOUT']
    digest=hashlib.sha256()
    with INPUT.open('wb') as f:
        header=f'{t1} {t2} {g}\n{N}\n'.encode();f.write(header);digest.update(header)
        batch=[]
        for i in range(N):
            a=i%4; valid=True
            if kind=='un_usuario':t,u=i*200,1999999
            elif kind=='muchos_usuarios':t,u=i//2000000,i%2000000
            elif kind=='uniforme_permutado':t,u=i//2000000,(i*104729)%2000000
            elif kind=='concentrado':t,u=i,1999999 if i%10 else (i//10)%1999999
            elif kind=='duplicados':t,u,a=i//100,1999999,0
            elif kind=='invalidos':
                t,u=i*200,1999999
                mode=i%8
                if mode:
                    bad=[None,f'{t}  1 READ',f'{t}\t1 READ',f'-{t} 1 READ',
                         f'{t} 2000000 READ',f'{t} 1 READ x',f'{t} 1 read',
                         '0000000000000 1 READ'][mode]
                    batch.append((bad+'\n').encode());valid=False
            elif kind=='max_longitud':t,u,a=995000001+i,1000000+i%1000000,3
            elif kind=='dentro_fuera':t,u=i,i%100000
            elif kind=='sin_brechas':t,u=i*200,1999999
            else:raise ValueError(kind)
            if valid:
                text=(f'{t:012d} {u:012d} {actions[a]}\n' if kind=='max_longitud'
                      else f'{t} {u} {actions[a]}\n')
                batch.append(text.encode())
                if t1<=t<=t2:
                    key=t*4+a
                    if last[u]!=key:
                        if counts[u]:
                            delta=t-(last[u]//4)
                            if delta<=g:sums[u]+=delta;nums[u]+=1
                        counts[u]+=1;last[u]=key
            if len(batch)>=10000:
                chunk=b''.join(batch);f.write(chunk);digest.update(chunk);batch=[]
        if batch:
            chunk=b''.join(batch);f.write(chunk);digest.update(chunk)
    top=sorted((u for u in range(2000000) if counts[u]),key=lambda u:(-counts[u],u))[:5]
    output=[]
    for u in top:
        avg='NA'
        if nums[u]:
            q=(sums[u]*1000+nums[u]//2)//nums[u]
            avg=f'{q//1000}.{q%1000:03d}'
        output.append(f'{u} {counts[u]} {avg}\n')
    return ''.join(output) or 'SIN DATOS\n',digest.hexdigest()

def main():
    results=[]
    names=['un_usuario','muchos_usuarios','uniforme_permutado','concentrado',
           'duplicados','invalidos','max_longitud','dentro_fuera','sin_brechas']
    for name in names:
        print('Generando',name,flush=True)
        expected,digest=generate(name)
        result=dict(name=name,lines=N,input_bytes=INPUT.stat().st_size,sha256=digest,
                    **bench(expected))
        results.append(result)
        (ROOT/'pruebas/estres_resultados.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
        print(result,flush=True)
    print('Finalizadas',len(results),'pruebas de 5 millones',flush=True)

if __name__=='__main__':main()
