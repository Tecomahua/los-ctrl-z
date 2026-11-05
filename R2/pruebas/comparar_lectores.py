from oraculo import ROOT
from estres import bench,generate,EXE
import estres
import subprocess,statistics,json,os

cpp=ROOT/'ejercicio1/codigo1.cpp'
code=cpp.read_text(encoding='utf-8')
start=code.index('class Input {')
end=code.index('\nInput input;',start)
getline='''class Input {
public:
    bool line(char* out, size_t capacity, int& length) {
        std::string s;
        if (!std::getline(std::cin, s)) return false;
        if (!s.empty() && s.back() == '\\r') s.pop_back();
        if (s.size() >= capacity) { length = -1; return true; }
        length = static_cast<int>(s.size());
        std::memcpy(out, s.c_str(), s.size() + 1);
        return true;
    }
};
'''
code=code[:start]+getline+code[end:]
code='#include <iostream>\n#include <string>\n'+code
code=code.replace('int main() {','int main() {\n    std::ios::sync_with_stdio(false);\n    std::cin.tie(nullptr);')
source=ROOT/'pruebas/getline.cpp'
source.write_text(code,encoding='utf-8')
baseline=ROOT/'pruebas/getline.exe'
compiler=os.environ.get('CXX','g++')
os.environ['PATH']=str(__import__('pathlib').Path(compiler).parent)+os.pathsep+os.environ['PATH']
subprocess.run([compiler,'-std=c++17','-O2',str(source),'-o',str(baseline)],check=True)
print('Generando max_longitud (12 digitos por campo, LOGOUT)',flush=True)
expected,digest=generate('max_longitud')
results={'input_bytes':estres.INPUT.stat().st_size,'sha256':digest,'fread':[],'getline':[]}
for _ in range(3):
    for name,exe in [('fread',EXE),('getline',baseline)]:
        estres.EXE=exe
        r=bench(expected);results[name].append(r)
        print(name,r,flush=True)
for name in ('fread','getline'):
    results[name+'_median_seconds']=statistics.median(r['seconds'] for r in results[name])
(ROOT/'pruebas/lectores_resultados.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(results,flush=True)
