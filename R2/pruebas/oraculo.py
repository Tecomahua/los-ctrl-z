from pathlib import Path
import subprocess, json, os

ROOT = Path(__file__).resolve().parents[1]
MATERIAL = Path(os.environ.get('AF_MATERIAL', ROOT / 'material/Ronda2_Avanzada/AF'))
ORACLE = Path(os.environ.get('AF_ORACLE', MATERIAL / ('caja_windows.exe' if os.name == 'nt' else 'caja_linux')))
LOG = ROOT / 'pruebas/experimentos.jsonl'

def run(data, exe=ORACLE):
    p = subprocess.run([str(exe)], input=data.encode(), capture_output=True, timeout=8)
    if p.returncode:
        raise RuntimeError((p.returncode, p.stderr.decode(errors='replace'), data))
    return p.stdout.decode()

def case(name, lines, header='0 1000000000 20', hypothesis=''):
    data = header + '\n' + str(len(lines)) + '\n' + '\n'.join(lines) + '\n'
    out = run(data)
    record = dict(name=name, hypothesis=hypothesis, input=data, output=out)
    with LOG.open('a', encoding='utf-8') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')
    print(name, repr(out))
    return out
