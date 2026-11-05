# Historial de prompts — A2: Pase express

**Competencia:** Prompt & Code Challenge 2026 · Ronda 1 · Categoría Avanzada  
**Equipo:** Los Ctrl + Z  
**Nombre recomendado del repositorio privado:** `los-ctrl-z`  
**IAs citadas:** Microsoft Copilot y Claude AI. ChatGPT realizó esta organización documental; Codex es el implementador previsto.

## Alcance y fidelidad documental

Este README conserva el **prompt textual aportado por el equipo** para A2 y las dos instrucciones dirigidas a Claude que figuran en el README de origen. Se respeta la redacción original. La exigencia de Python 3 expresa la preferencia del prompt de Copilot y no anula que las reglas oficiales permitan también C y C++.

No se dispone de los prompts específicos completos que se enviaron a Claude para generar `codigo2.cpp`; **no se reconstruyen ni se atribuyen falsamente**. Tampoco se dispone de resultados observados en la caja negra. El archivo oficial `conversacion2.md` (o `.txt`/`.json`) debe contener el chat íntegro real y los experimentos, y no puede sustituirse con este README.

## Historial: Microsoft Copilot

### P1 — Prompt definitivo compartido (A2)

```text
PROMPT DEFINITIVO - PROBLEMA A2

Necesito que resuelvas el siguiente problema de programación competitiva como si estuvieras participando en una final de ICPC, IOI o una competencia de nivel maestría.

La implementación final debe realizarse exclusivamente en Python 3.

Este problema incluye una caja negra oficial que acepta entradas pequeñas y devuelve respuestas correctas según las reglas reales del problema. El enunciado indica explícitamente que existen condiciones de uso del pase express que NO están completamente especificadas y que deben descubrirse mediante experimentación.

Por lo tanto, antes de programar, debes realizar ingeniería inversa del problema utilizando razonamiento y diseñando pruebas específicas para la caja negra.

No escribas código inmediatamente.

1. Comprensión del problema

Analiza cuidadosamente el enunciado e identifica:

Qué representan los N nodos.
Qué representan las M vías.
Qué significa que una vía sea bidireccional.
Qué representa el costo de una vía.
Qué representan los vértices:
S
T
U
V
Qué es un camino mínimo entre S y T.
Qué información debe imprimirse.
Qué significa que el resultado sea -1.
Qué papel cumple el pase express.

Después explica el problema con tus propias palabras.

2. Detección de ambigüedades

El enunciado indica explícitamente:

"Lo que debes descubrir con la caja negra: las condiciones de uso del pase."

Por lo tanto, antes de continuar debes identificar todas las posibles interpretaciones de esa frase.

Analiza preguntas como:

¿Qué vías exactamente se vuelven gratuitas?
¿Todas las vías del camino mínimo?
¿Solo algunas?
¿Se puede recorrer una vía gratuita varias veces?
¿Las vías gratuitas conservan alguna restricción?
¿Se puede utilizar únicamente una parte del camino mínimo?
¿Debe elegirse un único camino mínimo?
¿Qué ocurre cuando hay múltiples caminos mínimos?
¿Las vías gratuitas pueden utilizarse en cualquier dirección?
¿El pase se consume?
¿Tiene límite de uso?
¿Puede aprovecharse parcialmente?

Enumera todas las hipótesis razonables antes de diseñar la solución.

3. Ingeniería inversa mediante la caja negra

Antes de programar:

Diseña pruebas mínimas para descubrir las reglas reales del pase express.

Incluye casos que permitan verificar:

Caso 1

Camino mínimo único.

Objetivo: Determinar el comportamiento básico del pase.

Caso 2

Dos caminos mínimos distintos con mismo costo.

Objetivo: Determinar si ambos son elegibles.

Caso 3

Tres caminos mínimos.

Objetivo: Determinar si puede elegirse cualquiera.

Caso 4

U y V dentro del camino mínimo.

Objetivo: Medir el beneficio completo del pase.

Caso 5

U y V fuera del camino mínimo.

Objetivo: Medir beneficio indirecto.

Caso 6

U conectado a una parte del camino mínimo.

Objetivo: Entender cómo puede aprovecharse parcialmente.

Caso 7

Uso repetido de una vía del camino mínimo.

Objetivo: Descubrir si existen restricciones de reutilización.

Caso 8

Recorrido en sentido contrario.

Objetivo: Determinar si el beneficio respeta la bidireccionalidad.

Caso 9

Aristas paralelas.

Objetivo: Determinar cómo son tratadas.

Caso 10

Bucles.

Objetivo: Verificar si afectan la lógica.

Para cada prueba debes indicar:

Entrada.
Hipótesis analizada.
Resultado esperado según cada interpretación.
Conclusión obtenible a partir de la caja negra.
4. Análisis de restricciones

Restricciones:

1 ≤ N ≤ 200 000
0 ≤ M ≤ 400 000
1 ≤ w ≤ 4 × 10^13
Puede haber vías paralelas.
Puede haber bucles.
Tiempo límite: 10 s.
Memoria máxima: 128 MB.

Determina:

Complejidad temporal máxima aceptable.
Complejidad espacial máxima aceptable.
Algoritmos descartados.
Algoritmos candidatos.

Analiza explícitamente:

Floyd-Warshall.
Bellman-Ford.
Dijkstra.
Múltiples ejecuciones de Dijkstra.
Construcción de DAG de caminos mínimos.
Programación dinámica sobre grafos.

Justifica cada decisión.

5. Diseño de la solución

Antes de programar:

Describe el algoritmo óptimo.
Justifica formalmente por qué funciona.
Explica qué información debe conocerse sobre los caminos mínimos entre S y T.
Explica qué información debe conocerse para responder la consulta entre U y V.
Describe las estructuras de datos utilizadas.
Explica el flujo completo de ejecución.
Justifica matemáticamente la corrección.

Indica:

Complejidad temporal.
Complejidad espacial.
6. Validación manual

Antes de programar:

Reconstruye manualmente los ejemplos oficiales.
Explica por qué producen exactamente las salidas indicadas.
Verifica que tu interpretación del pase express coincide con los resultados.

Si no puedes explicar completamente los ejemplos, vuelve a analizar la teoría antes de escribir código.

7. Casos límite

Analiza explícitamente:

Grafo vacío.
M = 0.
U = V.
S = T.
U = S.
V = T.
Camino mínimo único.
Múltiples caminos mínimos.
Grafo árbol.
Grafo con ciclos.
Grafo muy denso.
Grafo muy disperso.
Aristas de costo máximo.
Aristas paralelas.
Bucles.
Casos sin conexión.
Casos cuya respuesta debe ser -1.

Explica cómo la solución maneja cada uno.

8. Implementación en Python

Solo después de completar todas las fases anteriores:

Genera una solución completa en Python 3.
Compatible con jueces automáticos.
Lectura desde stdin.
Escritura únicamente en stdout.
Sin librerías externas.
Sin impresiones de depuración.
Optimizada para N = 200 000 y M = 400 000.
Diseñada para evitar TLE y MLE.
Lista para envío directo al juez.
9. Verificación final

Antes de entregar el código:

Verifica nuevamente la interpretación descubierta mediante la caja negra.
Verifica que los ejemplos oficiales estén explicados correctamente.
Verifica la complejidad temporal.
Verifica la complejidad espacial.
Verifica todos los casos borde.
Identifica posibles riesgos de:
WA (Wrong Answer)
TLE (Time Limit Exceeded)
MLE (Memory Limit Exceeded)

No entregues código hasta tener una interpretación consistente del pase express respaldada por el enunciado, los ejemplos y las pruebas diseñadas para la caja negra.

Problema

Una ciudad tiene N estaciones y M vías bidireccionales con costo.

Tu viaje de trabajo va de S a T.

Tienes un pase express: eliges uno de los caminos de costo mínimo de S a T y las vías de ese camino te salen gratis, con ciertas condiciones de uso.

Debes imprimir el costo mínimo para ir de U a V, o -1 si no existe un camino.

Entrada:

Línea 1: N M
Línea 2: S T U V
Luego M líneas con:
a b w

Salida:

Un entero.

Límites:

1 ≤ N ≤ 200000
0 ≤ M ≤ 400000
1 ≤ w ≤ 4 × 10^13
Puede haber vías paralelas y bucles.
Tiempo: 10 s
Memoria: 128 MB
```

## Prompts dirigidos a Claude AI (comunes a A1 y A2)

**Procedencia:** `README.md` original compartido por el equipo. Ese documento registra dos instrucciones textuales dirigidas a Claude en el contexto de los dos problemas, pero no contiene una transcripción completa de la conversación.

### C1 — Solicitud original de solución

```text
Tiene que ser codigo funcional y a la vez con menos lineas de codigo basura, razonamiento, logica y rendimiento tomando en cuenta los factores que te dare en seguida
```

**Contexto registrado en el README de origen:** se adjuntó `Ronda1_Avanzada.pdf` y se dieron los criterios de calificación: funcionalidad 50 puntos, prompting 25, rendimiento 15 y tiempo de envío 10. El texto exacto de esos factores como mensaje separado no está disponible.

### C2 — Solicitud de documentación

```text
proporcioname en un redmi profecional los promps que te genere
```

> Estas son las únicas instrucciones textuales atribuidas a la conversación de Claude que aparecen en el README original. Su respuesta con algoritmos y supuestos es una **respuesta de IA**, no un prompt enviado por el equipo; por ello no se presenta como uno.

## Alcance de la entrega oficial

- Este README es un **índice y transcripción parcial de prompts facilitados al equipo**, no una exportación automática íntegra de Claude, Copilot, ChatGPT o Codex.
- El archivo `conversacion1.md` / `conversacion2.md` (según el ejercicio) debe conservar todas las intervenciones relevantes del historial real, incluidas las pruebas y las respuestas de la caja negra.
- No se han inventado respuestas ni atribuido ejecuciones no observadas.

## Prompt maestro y continuación en Codex

**M1 — Prompt maestro recibido por Codex.** El equipo adjuntó el texto íntegro titulado `PROMPT MAESTRO — PROMPT & CODE CHALLENGE 2026`. Se conserva sin recortes en [`../../PROMPT_MAESTRO.md`](../../PROMPT_MAESTRO.md). Sus fases A2.1–A2.3 solicitan descubrir las condiciones del pase mediante caja negra, auditar el enfoque de cuatro Dijkstra y DAG, contrastar con referencia exhaustiva y medir rendimiento. El prompt también abarca A1 y la entrega; se guarda una sola copia para preservar una fuente textual única. **Es un prompt aportado por el equipo, no una observación de la caja negra.**

**C3 — Solicitud actual del equipo a Codex, transcripción textual:**

```text
Vas a tomar en cuenta los siguientes README para incluirlos, añadiendo tu propuesta, y lo del codex maestro que te proporcione anteriormente, este va a ser una bitacora de prompts, así es el lineamiento original que requerimos, añadelo correctamente ya implementado en la carpeta correspondiente
```

Esta transcripción de un mensaje no pretende sustituir el chat completo.

## Propuesta técnica y ejecución local de Codex

El README técnico aportado para A2 se conserva fielmente en [`../../fuentes/README_A2_recibido.md`](../../fuentes/README_A2_recibido.md). Allí se describen el enunciado, las hipótesis anteriores y el plan de ingeniería inversa. La propuesta anterior atribuye a Claude un pase **bidireccional**; **el código actual solo permite avanzar de S hacia T** en un subcamino gratuito contiguo de un único camino mínimo, una vez. Ninguna de estas condiciones ha sido confirmada con la caja negra.

Codex implementó [`codigo2.cpp`](codigo2.cpp) en C++17 con cuatro Dijkstra y una DP sobre el DAG de caminos mínimos. Bajo **estas hipótesis provisionales**, compiló y coincidió con una referencia que enumera caminos simples mínimos en 302/302 casos locales: dos ejemplos y 300 grafos aleatorios con semilla fija. En un caso mixto de `N=200,000` y `M=400,000`, el tiempo local medido fue 0.709 s y el pico de memoria **muestreado** fue 27,430,912 bytes. El segundo ejemplo aportado declara `M=9`, pero contiene solo 8 vías: la prueba usó `M=8` y obtuvo `2`. La evidencia reproducible y sus límites figuran en [`../../ESTADO.md`](../../ESTADO.md).

**Registro de caja negra oficial:** en los materiales revisados no hay ejecuciones ni salidas oficiales de A2. Por tanto, dirección, continuidad y uso del pase descritos arriba siguen siendo hipótesis. Las 500 pruebas y cifras de rendimiento atribuidas a Claude en el README técnico carecen aquí de registros reproducibles y no se suman a los 302 casos locales ejecutados por Codex.

Este README es una **bitácora de prompts y procedencia**, no `conversacion2.md`. Falta exportar el historial íntegro y auténtico de las interacciones relevantes, incluidas futuras pruebas de caja negra, antes de considerar completa la entrega.
