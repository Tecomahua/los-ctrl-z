# Estado provisional — Prompt & Code Challenge 2026

Fecha local: 2026-11-05. Al iniciar solo estaba disponible el prompt maestro adjunto; la carpeta de trabajo estaba vacía. Después el equipo proporcionó dos README técnicos y un ZIP con dos bitácoras parciales de prompts, incorporados en `fuentes/` y `R1/ejercicio*/README.md`. No se encontró ejecutable oficial de caja negra ni código anterior de Claude.

## A1

- Archivo: `R1/ejercicio1/codigo1.cpp`.
- Semántica **no confirmada**: longitud por posiciones físicas, ceros ignorados en la mediana, tramos solo de ceros inválidos, mediana superior para longitud par.
- Algoritmo: prefijos de `+1/-1/0`, ventana de inicios `[j-R,j-L]`, frecuencias por valor de prefijo y suma de índices. La consulta `pref[inicio] <= pref[j]` se actualiza en O(1) porque cada nuevo elemento cambia el umbral a lo sumo en una unidad. Se descuentan los tramos solo de ceros.
- Complejidad: O(N) tiempo, O(N) memoria. La suma de longitudes usa `__int128`.
- Verificación local: compilación con `g++ -O2 -std=c++17`; 2 ejemplos y 300 casos aleatorios contrastados con referencia exhaustiva (302/302 bajo la semántica anterior).
- Benchmark local de N=4,000,000, L=123, R=2,345,678, mezcla periódica de ceros y valores: 0.227 s; pico de memoria muestreado: 116,310,016 bytes. Entrada generada por `generar_benchmarks.js`.
- Caso de todos los tramos válidos, N=4,000,000: salida `8000002000000 10666674666668000000`, demostrando la necesidad de más de 64 bits para la suma.

## A2

- Archivo: `R1/ejercicio2/codigo2.cpp`.
- Semántica **no confirmada**: un camino mínimo S→T elegido, un subcamino gratuito contiguo recorrido una vez en sentido S→T.
- Algoritmo: Dijkstra desde S, T, U y V; los vértices de algún camino mínimo S→T forman un DAG por distancia desde S, porque los pesos son positivos. La DP en el orden de extracción de Dijkstra propaga el mejor costo de llegada desde U y combina el costo de salida a V. Se considera también U→V sin pase.
- Complejidad: O((N+M) log N) tiempo, O(N+M) memoria. `INF=LLONG_MAX`; se evita desbordamiento antes de sumar. Una distancia simple máxima con estas restricciones es `(N-1)*4e13 = 7,999,960,000,000,000,000`, representable en `int64_t`.
- Verificación local: compilación con `g++ -O2 -std=c++17`; 2 ejemplos y 300 grafos aleatorios comparados con referencia que enumera caminos simples mínimos (302/302 bajo la semántica anterior).
- El ejemplo 2 del texto adjunto declara M=9 y contiene solo 8 líneas de vías. La prueba usó esas 8 vías y M=8; obtuvo la salida indicada `2`.
- Benchmark local con N=200,000, M=400,000 y vías mixtas: 0.709 s; pico de memoria muestreado: 27,430,912 bytes. Otro caso con cadena de peso 4×10¹³, S=T y N=200,000 produjo `7999960000000000000`.

## Pendientes para una entrega válida

1. Obtener y ejecutar las cajas negras oficiales. Probar las convenciones de mediana y ceros de A1, y dirección, reutilización y elección de caminos de A2. Corregir el código si alguna hipótesis falla.
2. Exportar e incorporar el historial **completo y auténtico** de conversaciones para cada ejercicio como `conversacion1.md` y `conversacion2.md`. No se han creado sustitutos ficticios.
3. El equipo se identifica en los README como **Los Ctrl + Z** y propone `los-ctrl-z` como nombre de repositorio, pendiente de validar con el staff. Esta carpeta no es un repositorio Git y no tiene remoto configurado. Crear el repositorio privado, agregar a `DanielaaER`, comprobar privacidad y archivos en GitHub, y enviar la URL al enlace oficial indicado por el staff.

Las pruebas diferenciales y los benchmarks solo validan los modelos provisionales y este entorno local. No prueban conformidad con las reglas ocultas ni aceptación en el juez.

## Registro de exportaciones y caja negra

El 2026-11-05 se revisó `Los_Ctrl_Z_Conversaciones_R1.zip`: contiene `R1/ejercicio1/conversacion1.md` (29,647 bytes) y `R1/ejercicio2/conversacion2.md` (21,726 bytes). Ambos archivos declaran que son extracciones temáticas y **no** exportaciones íntegras certificadas. Se conservan sin modificaciones para no hacerlas pasar por historiales completos. Cada uno refiere como fuente primaria el chat compartido <https://chatgpt.com/share/6aecb01d-7204-83e8-b329-aa35b545070c>; la consulta web solo devolvió el título de la página y la interfaz de navegador disponible falló al iniciarse. Por ello no fue posible obtener un volcado completo desde ese enlace.

Se buscaron ejecutables de caja negra entre los archivos del proyecto y archivos relevantes de `D:\Backup\Descargas`; no se encontró ninguno. Tampoco hay una URL de caja negra en los documentos disponibles. No se ejecutaron casos contra el juez oficial ni se registran salidas inventadas. Las pruebas y resultados locales anteriores siguen siendo los únicos disponibles y están sujetos a las hipótesis indicadas en las bitácoras A1 y A2.

**Estado comprobable:** no se registran exportaciones íntegras ni ejecuciones oficiales de caja negra en esta entrega. Las conversaciones conservan la nota de procedencia de los archivos fuente y las soluciones siguen identificadas como provisionales. No se atribuyen al juez resultados locales.
