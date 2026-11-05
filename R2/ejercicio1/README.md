# Solución AF: Transmisiones masivas

## Resultado y alcance

La entrega es [`codigo1.cpp`](codigo1.cpp), C++17 sin dependencias. Los experimentos
usan solamente entrada/salida de `caja_windows.exe`, sin inspeccionar su implementación.
No se afirma conocer los casos privados ni haber obtenido 100 % de funcionalidad.

Se leyó el PDF completo de tres páginas, se renderizó y revisó visualmente, y se
contrastó con `enunciado.md` y `LEEME_caja_negra.txt`. Los dos ejemplos oficiales
coincidieron con el oráculo y con la solución. Los binarios para otros sistemas se
conservaron sin ejecutarlos.

## Reglas y evidencia

CONFIRMADO por el enunciado: eventos ordenados por tiempo, intervalo inclusivo,
cuatro acciones, límites de timestamp/usuario, clasificación por conteo y después
por usuario, hasta cinco resultados, `NA` y `SIN DATOS`.

VERIFICADO experimentalmente, con confianza alta en los casos observados:

1. Un evento es duplicado si coincide en timestamp numérico y acción con el último
   evento contado de ese usuario. Otros usuarios no interrumpen la comparación.
   Repetir tres veces READ cuenta una; READ-WRITE-READ al mismo tiempo cuenta tres.
   No se mantiene un conjunto de todos los triples vistos.
2. Una brecha se incluye cuando `delta <= G`. Se verificaron G-1, G y G+1, G=0,
   brechas cero y el evento posterior a un corte. El evento del corte sí cuenta y
   reemplaza al predecesor. Las 16 parejas de acciones dan la misma regla temporal;
   LOGIN y LOGOUT no introducen lógica adicional de sesiones.
3. Cada línea de evento debe ajustarse a
   `[0-9]{1,12} [0-9]{1,12} (LOGIN|READ|WRITE|LOGOUT)`, con coincidencia completa,
   timestamp <= 10^9 y usuario < 2,000,000. Los dos separadores son espacios ASCII
   simples. Se rechazan signos, tabuladores, espacios dobles, campos extra,
   decimales, acciones con distinta capitalización y líneas vacías. Los ceros
   iniciales se aceptan hasta 12 dígitos; 13 ceros se rechazan aunque el valor sea 0.
4. Los eventos inválidos o fuera de [T1,T2] no cambian el estado usado en el cálculo.
5. Los promedios probados redondean al milésimo más cercano con mitad hacia arriba.
   Por ejemplo 17/16 -> 1.063 y 21/16 -> 1.313, lo que descarta mitad-par. Se
   probaron denominadores diferentes, periódicos, valores cercanos a mitad y sumas
   cercanas a 10^9. Se implementa redondeo racional exacto, sin punto flotante.

El modo texto de Windows traduce CRLF y trata Ctrl-Z como EOF. Además, el lector
elimina un CR residual. Estos controles se investigaron aparte y no se presentan
como reglas portables del juez. La solución conserva el modo de texto nativo y
acepta LF, CRLF y última línea sin salto. Las líneas largas se consumen completas
sin almacenarlas. Una prueba exploratoria desordenada mostró brechas negativas;
queda fuera del contrato y no se usa para demostrar la solución.

La formulación de estas reglas es una generalización de la evidencia disponible,
no una demostración sobre el código interno de la caja. El catálogo completo
[los registros anotados](../pruebas/experimentos_anotados.jsonl) y [los datos crudos](../pruebas/experimentos.jsonl) conservan cada
entrada, salida, hipótesis evaluada, interpretación y confianza. Dos sondeos de
2,001 líneas recibieron el error de límite N <= 300 del oráculo y se excluyeron de
las verificaciones de corrección; no se usó el oráculo en pruebas masivas.

## Algoritmo e invariantes

Para cada usuario se mantienen conteo, último timestamp/acción empaquetados,
cantidad de brechas incluidas y suma de esas brechas. Después de cualquier prefijo
del archivo, el último estado representa exactamente el último evento contado:
una línea descartada no lo modifica, un duplicado lo conserva y todo nuevo evento
lo reemplaza. Por tanto, la diferencia temporal se calcula siempre contra el
predecesor correcto. Agregarla si y sólo si no supera G mantiene por inducción la
suma y el denominador correctos.

Tras consumir N líneas, se recorren los usuarios de menor a mayor. Se inserta cada
candidato en una lista ordenada de capacidad cinco. Las igualdades permanecen detrás
de los usuarios ya visitados, de menor identificador. Así, tras cada candidato la
lista contiene los cinco mejores del prefijo y termina con el resultado requerido.

Tiempo: O(L + U), siendo L la cantidad de bytes de entrada y U = 2,000,000. Con
líneas de longitud limitada equivale a O(N + U). Memoria: O(U), independiente de N.
No hay ordenamiento global, mapas hash ni asignaciones por evento.

| Estado | Bytes por usuario | Total de bytes |
|---|---:|---:|
| Conteo, uint32_t | 4 | 8,000,000 |
| Timestamp/acción, uint32_t | 4 | 8,000,000 |
| Cantidad de brechas, uint32_t | 4 | 8,000,000 |
| Suma, int64_t | 8 | 16,000,000 |
| Total de arreglos | 20 | 40,000,000 |
| Buffer fread | — | 1,048,576 |

Arreglos más buffer: 41,048,576 bytes, aproximadamente 39.15 MiB, más objetos
pequeños, biblioteca y ejecutable. Los arreglos separados evitan el relleno de una
estructura por usuario. `(timestamp << 2) | accion` ocupa como máximo 4,000,000,003,
que cabe en uint32_t. Los contadores nunca superan cinco millones.

En entrada ordenada, las brechas incluidas son una parte de la suma telescópica:
la suma por usuario no supera 10^9. Escalarla por 1000 no supera 10^12. Se conserva
int64_t para margen adicional. El parser acumula a lo sumo 12 dígitos en uint64_t,
comprueba los límites antes de indexar y limita la línea almacenada a 127 bytes;
una línea válida ocupa a lo sumo 32 bytes antes del salto. Una línea inválida de
aproximadamente un MiB confirmó que se descarta completa sin perder la siguiente.

Para una suma S >= 0 y K brechas, el entero de milésimas se calcula como
`(1000*S + K/2) / K`. Si K es impar no puede existir una mitad exacta en el resto;
si es par la expresión redondea esa mitad hacia arriba. Se imprime la parte
entera y el residuo con exactamente tres dígitos.

## Verificación ejecutada

- GCC MSYS2 UCRT 15.2, `-std=c++17 -O2 -Wall -Wextra -Wconversion -Wshadow -pedantic`:
  compilación correcta sin advertencias.
- Dos ejemplos oficiales correctos.
- 3,000 entradas aleatorias, semilla 20261105, entre 1 y 300 líneas, comparadas byte
  por byte con el oráculo Windows: cero discrepancias. Incluyen empates, ceros,
  extremos de usuario, duplicados, intervalos, límites G y líneas inválidas.
- 224 regresiones dirigidas válidas para el oráculo: cero discrepancias. La primera
  ejecución aleatoria incluía 196; tras agregar 28 sondeos de bordes/redondeo se
  ejecutó toda la regresión ampliada. La función de reducción está implementada;
  no se activó porque no hubo discrepancias.
- Nueve escenarios de 5,000,000 de líneas, con referencia Python independiente
  calculada durante la generación: todas las salidas correctas.
- Escenario adicional de 5,000,000 de líneas y 165,000,032 bytes: seis ejecuciones
  correctas al comparar los lectores, tres por implementación.

Los dos generadores de pruebas usan sólo la biblioteca estándar de Python. El
modelo de estrés usa arreglos y la misma definición matemática de las reglas,
independiente del empaquetado y del lector C++.

| Escenario, 5 millones de líneas | Segundos | Pico residente, MiB |
|---|---:|---:|
| Un usuario | 0.6923 | 43.664 |
| Dos millones de usuarios | 0.4930 | 43.332 |
| Usuarios permutados uniformemente | 0.7428 | 43.328 |
| Distribución concentrada | 0.6353 | 14.734 |
| Duplicados abundantes | 0.5239 | 12.824 |
| 87.5 % de líneas inválidas | 0.4895 | 12.816 |
| Timestamps/usuarios de valores grandes | 1.0222 | 28.086 |
| Dentro/fuera del intervalo | 0.5730 | 14.348 |
| Ninguna brecha computable | 0.9372 | 12.816 |

Las cifras exactas, tamaños, SHA-256 de las entradas y salidas están en
[`estres_resultados.json`](../pruebas/estres_resultados.json). Se mide exclusivamente la ejecución del proceso hijo,
incluido su arranque y lectura, excluyendo la generación del archivo. Se consulta
`PeakWorkingSetSize` de Windows con intervalos de 1 ms y también el pico de memoria
privada comprometida. La memoria del generador Python no pertenece a la solución.
Es una observación del sistema operativo; la generación también puede influir en
la caché de archivos. Estos tiempos no se extrapolan como garantía del hardware
del juez. La primera tanda se ejecutó antes de añadir el formato con 12 dígitos al
generador; la comparación posterior cubre expresamente ese caso más largo.

Comparación controlada sobre el mismo archivo de 165 MB: mediana fread de 0.5995 s
frente a getline de 0.7827 s, tres ejecuciones por lector en orden alternado.
La mejora observada es aproximadamente 23.4 %. getline desactiva sincronización
con stdio y usa el mismo parser y algoritmo; las salidas coinciden. Se conserva
fread, que además mantiene el uso de memoria acotado ante líneas enormes.

El compilador predeterminado C:\MinGW no inicia correctamente; se sustituyó por
MSYS2. Ubuntu aparece registrado en WSL, pero no puede iniciar por
HCS_E_SERVICE_NOT_AVAILABLE. No se ejecutó validación Linux. El intento de compilar
con UBSan falló porque esa instalación de GCC no incluye libubsan: no se afirma
haber pasado sanitizadores. Estos fallos del entorno no se confundieron con
pruebas de la solución.

## Reproducción

Las [instrucciones y utilidades](../pruebas/README.md) están dentro de R2. Allí se
conservan las entradas/salidas y los resultados JSON de la sesión real, sin publicar
ejecutables del oráculo, binarios compilados ni entradas masivas. El código de la
entrega es independiente de estas herramientas.

## Conversación y prompting

`conversacion1.md` se genera a partir del registro real de esta sesión, con los
mensajes públicos y las llamadas/resultados de herramientas hasta un corte
declarado. Se incluye literalmente el prompt pegado, que llegó como archivo.
No se reconstruyen conversaciones, no se incluyen instrucciones internas ni
razonamiento privado. El corte no incluye las acciones ni la respuesta que ocurran
después de exportarlo; por ello no se presenta como exportación de mensajes futuros.
La exportación se actualiza desde el registro local disponible en esta conversación.
El corte vigente se declara al principio del archivo conversacional.


## Bitácora de integración — 5 de noviembre de 2026

El usuario indicó usar el mismo repositorio `Tecomahua/los-ctrl-z`, conservar R1 y
organizar la Ronda 2 según la imagen de entrega. Se comprobó que el historial
existente usa el mensaje de commit `R1`; los commits de esta entrega usan `R2`.

Se añadió la solución C++17 y la conversación original en `R2/ejercicio1/`, este
informe como README del ejercicio y las utilidades/evidencias en `R2/pruebas/`.
El README principal incorpora los enlaces y los resultados reales. El código
conserva el mismo contenido SHA-256 validado en la primera fase:
`8f405c9782c32170135f4b5470cce9deeafb5542d5400b604cfae4ce66739ecf`.

La base de integración es el commit `a37d9513fd80a4939affc4dce629ef2fa0245d51`.
El árbol original de R1 es `4a20dd20fb9e42ed0e63fd3f6d56147cb9b88790`; su igualdad
en el árbol propuesto permite verificar que sus archivos permanecen idénticos.
La integración se propone en el [pull request #1 — R2: Transmisiones masivas (AF)](https://github.com/Tecomahua/los-ctrl-z/pull/1),
desde `codex/r2-transmisiones-masivas` hacia `main`. El primer commit `R2` es
`341dd45cb63704725281eea9e2a061d84d49926c`. GitHub confirmó que el pull request
está abierto, sin conflictos; no se encontraron ejecuciones de CI en esa revisión.
El diff contiene únicamente `README.md` y rutas dentro de `R2/`, con R1 idéntico
al árbol original. La conversación exportada se renovó después de abrir el PR,
conservando un corte explícito para los mensajes posteriores.

Al adaptar las rutas de las utilidades para el repositorio, se recompiló el mismo
código con GCC 15.2 y C++17, sin advertencias. Se repitieron los dos ejemplos y las
224 regresiones desde `R2/pruebas/`: todos coincidieron byte por byte con la caja
negra (6.859 s para la ejecución completa de esta regresión). Las 3,000 aleatorias
y las mediciones masivas anteriores permanecen registradas con su procedencia;
no se presentan como nuevas ejecuciones de esta fase de organización.

La hora de entrega depende del último commit sobre `R2/ejercicio1/`, según las
indicaciones aportadas por el usuario. Las actualizaciones siguientes de esta
conversación deben reflejarse aquí con sus resultados verificables y renovar la
exportación real; una bitácora resumida no reemplaza los mensajes originales.
