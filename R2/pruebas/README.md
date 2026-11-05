# Pruebas de Ronda 2

Estas utilidades reproducen la comparación con la caja negra y las mediciones de
la solución. Requieren Python 3 y un compilador C++17. No requieren paquetes de
Python externos. El oráculo y los ejemplos se obtienen del ZIP oficial; no se
publican sus ejecutables en este repositorio.

## Compilar y comparar

Desde la raíz del repositorio, en PowerShell:

```powershell
g++ -std=c++17 -O2 -Wall -Wextra -Wconversion -Wshadow -pedantic R2/ejercicio1/codigo1.cpp -o R2/pruebas/codigo1.exe
$env:AF_MATERIAL = 'C:\ruta\Ronda2_Avanzada\AF'
python R2/pruebas/diferencial.py 0
python R2/pruebas/diferencial.py 3000
```

`AF_MATERIAL` apunta al directorio que contiene `ejemplo1.in`, `ejemplo2.in` y el
ejecutable de referencia. También pueden establecerse `AF_ORACLE` y `AF_SOLUTION`
para elegir los ejecutables. En Linux el nombre predeterminado de la solución es
`R2/pruebas/codigo1` y el del oráculo es `caja_linux`; sus permisos de ejecución
deben habilitarse. Esa ruta Linux está preparada, pero no fue ejecutada en esta
sesión porque WSL no pudo iniciar.

`experimentos.jsonl` conserva 226 sondeos reales: 224 son regresiones; dos fueron
rechazados por superar el límite de 300 líneas del oráculo. El comparador excluye
estos dos y nunca usa la caja negra con cinco millones de líneas. El archivo
`experimentos_anotados.jsonl` añade hipótesis, interpretación y confianza. Los
controles CR/Ctrl-Z conservan el comportamiento nativo de la plataforma; las
salidas históricas guardadas fueron obtenidas en Windows. La comparación vuelve
a ejecutar ambos programas y exige igualdad byte por byte en la plataforma usada.

Las 3,000 entradas aleatorias usan semilla `20261105`. Ante una discrepancia se
reduce la entrada y se guarda como `discrepancia.in`. No hubo discrepancias en la
ejecución original, por lo que no se activó la reducción.

## Estrés y lectores

Las mediciones de memoria usan la API de Windows. Desde la raíz:

```powershell
python R2/pruebas/estres.py
# CXX permite elegir el compilador de la variante getline:
$env:CXX = 'g++'
python R2/pruebas/comparar_lectores.py
```

El generador escribe un único `estres.in` a la vez, calcula su salida con un modelo
Python independiente y mide solamente el proceso C++. No consulta el oráculo.
El archivo puede alcanzar 165 MB. El pico residente se obtiene de
`PeakWorkingSetSize`; se registra además la memoria privada comprometida.

Los archivos `*_resultado.json`, `estres_resultados.json` y
`lectores_resultados.json` conservan los resultados reales de la primera sesión.
Una nueva ejecución reemplaza el resumen correspondiente, pero no los datos de
otros tipos de prueba. La comparación de lectores genera `getline.cpp` y sus
ejecutables únicamente como archivos locales.

La tanda original de nueve escenarios usó campos numéricos sin rellenar. El
generador se amplió después para representar el escenario `max_longitud` con
12 dígitos por campo y LOGOUT. Esa versión de 165,000,032 bytes se ejecutó en la
comparación de lectores. Los hashes históricos permiten distinguir ambas entradas.

Los binarios, entradas masivas, archivos temporales y nuevas discrepancias se
excluyen mediante `.gitignore`. Se conservan los datos pequeños necesarios para
reproducir la evidencia del [informe](../ejercicio1/README.md).
