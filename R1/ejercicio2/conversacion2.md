# Prompt & Code Challenge 2026 — Conversación A2: pase express

**Equipo:** Los Ctrl + Z  
**Repositorio privado previsto:** `los-ctrl-z`  
**Ronda:** 1 · Categoría Avanzada  
**Fuente primaria del chat compartido:** [https://chatgpt.com/share/6aecb01d-7204-83e8-b329-aa35b545070c](https://chatgpt.com/share/6aecb01d-7204-83e8-b329-aa35b545070c)

> **Nota de procedencia:** este documento reúne los textos originales proporcionados en esta conversación, incluyendo prompts enviados por el usuario, propuestas pegadas desde Copilot/Claude y prompts redactados aquí para Codex. El enlace anterior es la referencia canónica del historial compartido. **Este Markdown es una extracción temática elaborada a partir de contenido recuperable, no un volcado automático, íntegro ni certificado de todos los mensajes y metadatos del enlace.** Las conversaciones originales independientes de Copilot, Claude y futuras sesiones de Codex no están incluidas salvo por los textos que el usuario pegó aquí. No se atribuyen pruebas de caja negra no realizadas.

**Convención:** cuando se identifica «Copilot (texto pegado por el usuario)» o «Claude (respuesta pegada por el usuario)», esa autoría proviene de la atribución del usuario, no de una exportación directa de la plataforma externa.

**Alcance del ejercicio:** A2 (`R1/ejercicio2/`).
## Contexto común — reglas de entrega aportadas por el usuario

Este mensaje se compartió literalmente en el chat. Sirve para ambos ejercicios.

~~~text
PROMPT & CODE CHALLENGE 2026 - COMO ENTREGAR TU SOLUCION
=========================================================

QUE ENTREGAS EN CADA EJERCICIO
  1. Codigo (obligatorio): tu programa final, en UN solo archivo (.py, .c o .cpp).
  2. Conversacion (obligatoria): el chat completo con tu IA, exportado (.md, .txt o .json).
     Debe incluir tus pruebas con la caja negra y lo que descubriste.
     Sin conversacion, el prompting de ese ejercicio vale 0.
  3. Bitacora (opcional): notas de lo que probaste y descubriste.

PASO A PASO
  1. Crea un repositorio PRIVADO en GitHub con el NOMBRE DE TU EQUIPO
     (uno por equipo; sin espacios, usa guiones: por ejemplo los-pythonistas).
  2. Agrega a DanielaaER como colaboradora:
     GitHub > Settings > Collaborators > Add people.
  3. Crea las carpetas de abajo y copia tu codigo y tu conversacion.
  4. Sube todo:   git add .   /   git commit -m "R1"   /   git push
  5. Verifica en github.com que se vean tus archivos.
  6. Envia la URL de tu repositorio en el enlace que indique el staff.

ESTRUCTURA DEL REPOSITORIO (respeta los nombres)
  nombre-de-tu-equipo/
  |-- R1/
  |   |-- ejercicio1/
  |   |   |-- codigo1.py            (o codigo1.c / codigo1.cpp)
  |   |   `-- conversacion1.md
  |   `-- ejercicio2/
  |       |-- codigo2.py
  |       `-- conversacion2.md
  `-- R2/                           (solo finalistas)
      `-- ejercicio1/
          |-- codigo1.py
          `-- conversacion1.md

  Los nombres deben empezar con "codigo" y "conversacion".
  Si no los encontramos, ese ejercicio cuenta como no entregado.

TU CODIGO
  - Lenguajes que se juzgan: Python, C y C++.
  - Lee de la entrada estandar y escribe en la salida estandar (igual que la caja negra).
  - Respeta el tiempo y la memoria que indica cada enunciado.

COMO SE CALIFICA CADA EJERCICIO (100 puntos)
  50  Funcionalidad: casos de prueba que resuelves bien.
  25  Prompting: calidad de tu conversacion con la IA.
  15  Rendimiento: casos que corren dentro de los limites de tiempo y memoria.
  10  Tiempo de envio: entre mas pronto entregues, mas puntos (solo si tu solucion es aceptada).

RONDAS
  - Ronda 1 (carpeta R1): 2 ejercicios. Tu puntaje es el promedio de los dos.
    Los 5 mejores de cada categoria pasan a la Ronda 2.
  - Ronda 2 (carpeta R2): 1 ejercicio, solo para finalistas. Se califica aparte.

HORA DE ENTREGA
  Tu hora de entrega es la hora del ULTIMO commit de la carpeta del ejercicio.
  Cuando termines un ejercicio, no vuelvas a modificar esa carpeta.
  La hora limite la anuncia el staff.

IMPORTANTE
  - La IA es tuya. Las cuotas o caidas de tu cuenta no dan prorroga.
  - Antes de entregar: nombres exactos, tu codigo corre con el ejemplo del enunciado,
    la conversacion esta completa, el repositorio se llama como tu equipo, es privado y DanielaaER es colaboradora.

Mucho exito!
~~~

## Asignación de responsabilidades

**Usuario:**

~~~text
te vas a encargar principalmente de la ingenieria de prompts, es decir; tu no vas a desarrollar la implementación, solamente me vas a dar ideas, para poder llevar a cabo el desarrollo te voy a proporcionar asímismo 2 opiniones de 2 IAS existentes (Claude AI, Copilot), vas a tomar la mejor decisión objetiva, de acuerdo a los requerimientos, no quiero que tengas favoritismo por ninguna
~~~

**Respuesta de ChatGPT — acuerdo esencial:** diseño y evaluación de prompts; la implementación de código corresponde a Codex; comparación técnica imparcial de Claude y Copilot. Esta oración se incluye como contexto editorial, no como cita literal del mensaje completo.

## A2/A1 · Respuesta técnica previa de Claude

**Interviniente:** Usuario (respuesta de Claude pegada en ChatGPT)

~~~text
Dejé los dos programas listos, pero no pude descubrir las reglas ocultas. No tengo el ejecutable de la caja negra, solo el PDF. Además, ninguno de los 4 ejemplos distingue las variantes posibles, porque no hay ceros en A1 y A2 da lo mismo con las dos lecturas del pase.

Lo que sí quedó confirmado: la mediana de A1 se compara con ≥ M, ya que el ejemplo 1 cuenta tramos con mediana 5 y otros con mediana 2 siendo M=2. Los dos programas reproducen los 4 ejemplos y coinciden con una fuerza bruta en pruebas aleatorias pequeñas (600 casos en A1, 500 en A2).

Rendimiento
A1: corre en O(N), con N=4·10⁶ tarda 0.13 s y usa unos 110 MB (límite 24 s / 256 MB).
A2: son 4 Dijkstra más una pasada sobre los caminos mínimos; con N=2·10⁵ y M=4·10⁵ tarda 0.73 s (límite 10 s / 128 MB).

Pruebas para correr en la caja

Cada una decide una constante que está al inicio del código. Pásame los resultados y ajusto lo que haga falta.

A1 (codigo1.cpp)

Entrada — Salida — Significa
2 2 2 3 / 1 5 — 0 0 — mediana inferior (UP=0, el valor actual)
                 — 1 2 — superior o promedio → corre la siguiente
2 2 2 3 / 1 4 — 1 2 — mediana superior → UP=1
                 — 0 0 — promedio → hay que reescribir esa parte
3 1 1 3 / 0 5 0 — 1 1 — el tamaño cuenta posiciones (supuesto actual)
                 — 4 8 — el tamaño cuenta solo lecturas válidas → hay que cambiar el algoritmo
3 3 3 5 / 5 0 0 — 1 3 — el 0 se ignora en la mediana (supuesto actual)
                 — 0 0 — el 0 cuenta como valor

A2 (codigo2.cpp)

Entrada — Salida — Significa
2 1 / 1 2 2 1 / 1 2 5 — 0 — vías gratis en ambos sentidos (BOTH=1, el valor actual)
                    — 5 — solo en el sentido S→T → BOTH=0
3 2 / 1 3 2 3 / 1 2 1 / 2 3 1 — 0 — se puede usar solo un tramo del camino (supuesto actual)
                    — 1 — hay que usar el camino completo → cambia la lógica

Mi código asume lo más probable en cada caso: en A1, el 0 se ignora en la mediana, el tamaño se mide en posiciones y un tramo sin lecturas válidas no cuenta. En A2, las vías gratis valen en ambos sentidos.

Para la entrega, el score de prompting depende de que la conversación exportada incluya tus pruebas con la caja y lo que descubriste. Corre esos casos en el chat y pega las salidas.

Te envié codigo1.cpp y codigo2.cpp. Corre las pruebas de las tablas en la caja negra y pásame las salidas para ajustar las constantes UP y BOTH, o reescribir la lógica si algún resultado lo pide.
~~~

## Discusión en ChatGPT sobre el algoritmo A2 de Claude

El usuario presentó la idea atribuida a Claude: cuatro Dijkstra y una pasada sobre las aristas de caminos mínimos, con hipótesis de gratuidad bidireccional. No se aportó `codigo2.cpp`, de modo que **no hay código fuente A2 externo para auditar literalmente**. ChatGPT señaló la necesidad de comprobar que las aristas gratuitas utilizadas sean compatibles con un solo camino mínimo elegible.

**Esta es una síntesis editorial de mensajes del chat compartido, no un volcado literal de sus respuestas.**

## A2 · Prompt definitivo de Copilot compartido por usuario

**Interviniente:** Usuario (texto atribuido a Microsoft Copilot)

~~~text
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
~~~

## Respuesta de ChatGPT — evaluación de Copilot para A2

Se reconoció la cobertura conceptual del prompt de Copilot, pero se cuestionó imponer Python por los 128 MB y 10 s; también se recomendó convertir las hipótesis de caja negra en entradas concretas y revisar distancias numéricas potencialmente cercanas a 8×10¹⁸. **Resumen editorial, no mensaje literal íntegro.**

## A2 · Prompt optimizado para Codex

**Interviniente:** ChatGPT (prompt redactado en esta conversación)

~~~text
Actúa como especialista ICPC en grafos ponderados, caminos mínimos y validación experimental.

Problema A2 — Prompt & Code Challenge 2026, categoría Avanzada.

Restricciones: N ≤ 200000, M ≤ 400000, pesos positivos hasta 4×10¹³, aristas paralelas y bucles. Tiempo 10 s, memoria 128 MB.

Objetivo: encontrar el costo mínimo de U a V utilizando un pase que permite elegir uno de los caminos mínimos de S a T y obtener gratuidad bajo condiciones ocultas.

**1. Descubre las reglas antes de implementar.**

Ejecuta pruebas pequeñas con la caja negra oficial para determinar:
- Si el pase funciona en ambos sentidos.
- Si permite utilizar subcaminos.
- Si puede elegirse cualquier camino mínimo.
- Si se libera un único camino o la unión de todos.
- Qué ocurre cuando S y T están desconectados.
- Qué ocurre cuando S=T o U=V.

Diseña entradas discriminantes. Registra salidas reales, interpretaciones descartadas y conclusiones confirmadas. No inventes resultados.

**2. Audita el algoritmo candidato de Claude.**

La propuesta utiliza cuatro ejecuciones de Dijkstra, construcción de un DAG de caminos mínimos entre S y T y programación dinámica.

Determina si es correcta bajo las reglas descubiertas.

Especialmente, verifica que:
- Las vías gratuitas correspondan a UN MISMO camino mínimo elegible.
- No se mezclen arbitrariamente aristas de caminos incompatibles.
- La programación dinámica respete el orden y dirección requeridos.
- Se consideren todos los puntos posibles de entrada y salida al trayecto gratuito.
- Se utilicen tipos numéricos seguros para distancias y sumas intermedias.
- Se manejen correctamente bucles, aristas paralelas y componentes desconectados.

**3. Evalúa eficiencia.**

Busca complejidad O((N+M)log N), o mejor, con memoria inferior a 128 MB.
Utiliza preferentemente C++17 si la evaluación objetiva de recursos lo justifica.
Evita estructuras duplicadas, asignaciones innecesarias y cálculos redundantes.

**4. Valida exhaustivamente.**

Construye una referencia de fuerza bruta para grafos pequeños bajo las reglas confirmadas.
Compara los resultados de la solución optimizada contra esa referencia mediante pruebas aleatorias y casos adversariales.
Verifica también los ejemplos oficiales y realiza mediciones de tiempo y memoria con entradas grandes.

**5. Entrega primero un informe breve.**

Incluye reglas confirmadas, evidencia, algoritmo, justificación de corrección, complejidad y riesgos.
No generes la implementación definitiva hasta terminar la validación semántica.
Conserva toda la conversación y las pruebas de caja negra para la entrega obligatoria.
~~~

## Prompt maestro conjunto para Codex — apartado A2

El chat incluyó un prompt maestro extenso para **A1 y A2**. Se conserva aquí una síntesis de su apartado A2 y el enlace original contiene el texto completo.

Actúa como un ingeniero de software senior especializado en programación competitiva ICPC, algoritmos avanzados, optimización de CPU/RAM, pruebas diferenciales e ingeniería inversa de programas de caja negra.

Estás participando en el Prompt & Code Challenge 2026 — Ronda 1, Categoría Avanzada.

Tu responsabilidad es llevar ambos problemas desde el análisis hasta una implementación funcional, probada y preparada para el juez automático.

Prioridades, en orden:
1. Corrección conforme a las reglas reales del juez.
2. Descubrimiento experimental de reglas ocultas.
3. Cumplimiento de los límites de tiempo y memoria.
4. Validación exhaustiva y reproducible.
5. Mínimo número de iteraciones y envíos.
6. Preparación de los archivos oficiales de entrega.

Reglas de trabajo: C++17 preferente; un archivo por ejercicio, stdin/stdout, sin librerías externas ni depuración en stdout; no inventar mediciones; validar caja negra; pruebas diferenciales; preparar archivos obligatorios y mantener historial íntegro. [Esta sección es una síntesis contextual, no cita literal del prompt maestro completo; consultar enlace compartido para el texto íntegro.]

PROBLEMA A2 — PASE EXPRESS
N ≤ 200,000; M ≤ 400,000; peso ≤ 4×10¹³; tiempo 10 s; memoria 128 MB.

Descubre mediante caja negra dirección gratuita, subtramos, elección de camino mínimo, si se permiten combinaciones de vías, reutilización, S=T y desconexión. Pruebas iniciales P1-P4: (2 1/1 2 2 1/1 2 5), (3 2/1 3 2 3/1 2 1/2 3 1), (4 4/1 4 2 3/1 2 1/2 4 1/1 3 1/3 4 1), (4 2/1 2 3 4/1 3 2/3 4 2).

Audita la estrategia candidata de cuatro Dijkstra y DAG con DP sin asumir que todas las vías de cualquier camino son simultáneamente gratuitas. Incluye viajes U→V sin pase, desconexiones, overflow (hasta 8×10¹⁸), bucles y aristas paralelas. Implementa C++17, prueba con referencia exhaustiva pequeña, aleatorios reproducibles y benchmarks extremos. Prepara `codigo2.cpp` y conversación real. [Síntesis temática; original completo en el chat compartido.]


## Historial mínimo de prompts dirigidos a Claude (compartido en README)

### Prompt dirigido a Claude — Solicitud original

~~~text
Tiene que ser codigo funcional y a la vez con menos lineas de codigo basura, razonamiento, logica y rendimiento tomando en cuenta los factores que te dare en seguida
~~~

### Prompt dirigido a Claude — Solicitud de documentación

~~~text
proporcioname en un redmi profecional los promps que te genere
~~~

**Fuente:** README original aportado por el equipo. No es una exportación completa del chat con Claude.

## Estado de evidencia

- **Cajas negras A2:** se propusieron pruebas sobre dirección, subcaminos, caminos mínimos alternativos y desconexiones, pero no se adjuntaron salidas reales.
- **Código A2 de Claude:** no fue facilitado; únicamente se compartió su descripción.
- **Pruebas comunicadas por Claude:** 500 aleatorias y benchmark de 0.73 s, afirmaciones no verificadas independientemente.
- **Implementación final por Codex:** pendiente al preparar este documento.
- **Para una entrega certificablemente íntegra:** agregar la conversación auténtica de Codex, las ejecuciones de la caja y cualquier ajuste realizado.
