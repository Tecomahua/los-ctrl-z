# PROMPT MAESTRO — PROMPT & CODE CHALLENGE 2026

## ROL Y OBJETIVO

Actúa como un ingeniero de software senior especializado en programación competitiva ICPC, algoritmos avanzados, optimización de CPU/RAM, pruebas diferenciales e ingeniería inversa de programas de caja negra.

Estás participando en el **Prompt & Code Challenge 2026 — Ronda 1, Categoría Avanzada**.

Tu responsabilidad es llevar ambos problemas desde el análisis hasta una implementación funcional, probada y preparada para el juez automático.

**Prioridades, en orden:**

1. Corrección conforme a las reglas reales del juez.
2. Descubrimiento experimental de reglas ocultas.
3. Cumplimiento de los límites de tiempo y memoria.
4. Validación exhaustiva y reproducible.
5. Mínimo número de iteraciones y envíos.
6. Preparación de los archivos oficiales de entrega.

No busques simplemente pasar los ejemplos. Busca maximizar los casos de prueba aceptados.

## REGLAS DE TRABAJO

- Lenguaje preferente: C++17, por razones de rendimiento y control de memoria.
- Código final en un solo archivo por ejercicio.
- Entrada mediante stdin; salida exclusivamente mediante stdout.
- No utilizar librerías externas.
- No introducir mensajes de depuración en stdout.
- No asumir que una solución anterior es correcta.
- No inventar ejecuciones, resultados, tiempos ni mediciones.
- No modificar código funcional sin una justificación técnica.
- No detenerte después de explicar un algoritmo: debes implementarlo y probarlo.
- Si una estrategia falla, identifica el contraejemplo y corrige su causa.
- Prioriza pruebas de alto valor informativo sobre miles de ejecuciones redundantes.
- No utilices la caja negra con entradas grandes: está destinada a pruebas pequeñas.
- Mantén registro fiel de los prompts, experimentos, errores y correcciones.

Trabaja de forma autónoma con los archivos y herramientas disponibles. Si una herramienta esencial falta, continúa con las verificaciones posibles y reporta exactamente qué quedó sin confirmar.

---

# PROBLEMA A1 — LATENCIAS Y MEDIANAS

## Enunciado

Disponemos de N latencias. Un valor 0 representa una lectura perdida.

Un tramo consecutivo [i,j] cuenta si su tamaño está entre L y R y su mediana es mayor o igual que M.

Debes imprimir dos enteros:

1. Cantidad de tramos válidos.
2. Suma de sus longitudes j-i+1.

Entrada:

- Primera línea: N L R M
- Segunda línea: N enteros ai.

Restricciones:

- 1 ≤ L ≤ R ≤ N ≤ 4,000,000.
- 0 ≤ ai ≤ 10⁹.
- 1 ≤ M ≤ 10⁹.
- Tiempo: 24 segundos.
- Memoria: 256 MB.

Ejemplo 1:

Entrada:
```text
7 3 7 2
2 1 4 2 2 5 6
```

Salida:
```text
15 65
```

Ejemplo 2:

Entrada:
```text
9 5 9 3
4 2 5 5 2 4 6 1 6
```

Salida:
```text
15 95
```

IMPORTANTE: ambos ejemplos cuentan todos los subarreglos de las longitudes permitidas. No son suficientes para determinar las reglas de mediana o ceros.

## FASE A1.1 — DESCUBRIMIENTO DE REGLAS

Localiza el ejecutable oficial de caja negra correspondiente a A1.

Determina experimentalmente:

- Mediana inferior, superior, promedio u otra convención para cantidades pares.
- Si los ceros participan en la mediana, se ignoran o invalidan tramos.
- Si el tamaño se mide por posiciones físicas o lecturas válidas.
- Si los tramos sin lecturas válidas cuentan.
- Cómo se calcula la longitud acumulada.

Pruebas iniciales, cada una en una ejecución independiente:

```text
2 2 2 3
1 5
```

```text
2 2 2 3
1 4
```

```text
3 1 1 3
0 5 0
```

```text
3 3 3 5
5 0 0
```

```text
3 3 3 5
9 0 1
```

```text
3 2 3 5
0 0 0
```

No asumas que estas seis pruebas distinguen todas las interpretaciones.

Para cada experimento:

1. Formula las hipótesis.
2. Calcula las salidas esperadas bajo cada hipótesis.
3. Ejecuta la caja negra.
4. Registra la salida observada.
5. Descarta únicamente las hipótesis incompatibles.
6. Si quedan ambigüedades, diseña otra prueba discriminante.

No avances a considerar definitiva una interpretación hasta tener evidencia suficiente.

## FASE A1.2 — ALGORITMO

Existe una propuesta previa de Claude con complejidad O(N), utilizando:

- Transformación de valores respecto a M.
- Sumas prefijas.
- Ventana deslizante.
- Arreglos de frecuencias.
- Sumas de índices para calcular longitudes.

Si su código está disponible, audítalo y reutilízalo únicamente cuando sea correcto. Si no está disponible, desarrolla la solución a partir de las reglas confirmadas.

Comprueba:

- Equivalencia matemática entre la condición de mediana y la condición sobre prefijos.
- Manejo de tramos con ceros.
- Inclusión de extremos L y R.
- Correcta actualización de la ventana.
- Conteo y suma de longitudes sin doble conteo.
- Invariantes de cada estructura.
- Desbordamiento de enteros.
- Memoria realmente utilizada.

Para N=4,000,000, la suma de longitudes puede exceder un entero con signo de 64 bits. Utiliza tipos adecuados y verifica también los productos intermedios.

Busca O(N) cuando las reglas lo permitan. Si necesitas otra complejidad, justifica que sea viable dentro de 24 segundos.

## FASE A1.3 — PRUEBAS

Construye un algoritmo de referencia independiente y exhaustivo para N pequeño, con la semántica confirmada.

Compara contra la solución optimizada:

- Ejemplos oficiales.
- Casos de caja negra.
- Casos aleatorios pequeños.
- Valores iguales.
- Valores inferiores y superiores a M.
- Alternancia de valores altos y bajos.
- Bloques de ceros.
- Todos los ceros.
- L=1, L=R, R=N.
- Ningún tramo válido.
- Todos los tramos válidos.

Ante cada discrepancia, conserva la entrada y explica su causa.

Después ejecuta benchmarks de tamaño grande y mide tiempo y memoria máxima.

---

# PROBLEMA A2 — PASE EXPRESS

## Enunciado

Tenemos N estaciones y M vías bidireccionales ponderadas.

El viaje habitual es de S a T. Se puede elegir uno de los caminos de costo mínimo entre esos vértices y obtener gratuidad en sus vías, bajo condiciones ocultas.

Debes determinar el costo mínimo de viajar de U a V, o -1 si no es posible.

Entrada:

- Primera línea: N M.
- Segunda línea: S T U V.
- M líneas: a b w.

Restricciones:

- N ≤ 200,000.
- M ≤ 400,000.
- 1 ≤ w ≤ 4×10¹³.
- Se permiten aristas paralelas y bucles.
- Tiempo: 10 segundos.
- Memoria: 128 MB.

Ejemplo 1:

Entrada:
```text
4 5
4 2 3 2
4 1 7
2 4 8
1 1 3
3 4 9
4 2 7
```

Salida:
```text
9
```

Ejemplo 2:

Entrada:
```text
4 9
3 4 1 2
2 3 2
1 3 1
4 2 3
4 1 1
4 2 2
4 4 3
2 4 2
2 2 1
```

Salida:
```text
2
```

## FASE A2.1 — INGENIERÍA INVERSA

Utiliza la caja negra oficial para descubrir las condiciones de uso del pase.

Investiga específicamente:

1. Si las vías son gratuitas en ambos sentidos.
2. Si el pase solo permite avanzar de S hacia T.
3. Si se puede utilizar un subcamino.
4. Si puede elegirse cualquiera de los caminos mínimos.
5. Si las vías gratuitas pertenecen a un único camino seleccionado.
6. Si el pase permite múltiples utilizaciones.
7. Qué ocurre con S=T.
8. Qué sucede cuando S y T están desconectados.
9. Cómo afectan las vías paralelas y los bucles.

Pruebas iniciales:

P1 — Dirección:
```text
2 1
1 2 2 1
1 2 5
```

P2 — Subcamino:
```text
3 2
1 3 2 3
1 2 1
2 3 1
```

P3 — Caminos mínimos alternativos:
```text
4 4
1 4 2 3
1 2 1
2 4 1
1 3 1
3 4 1
```

P4 — Desconexión entre S y T:
```text
4 2
1 2 3 4
1 3 2
3 4 2
```

Diseña experimentos adicionales sobre reutilización del pase, direcciones, recorridos parciales y caminos alternativos.

No concluyas que todas las vías pertenecientes a algún camino mínimo se pueden usar gratuitamente en una misma ruta. Debes respetar la elección de un único camino cuando corresponda.

## FASE A2.2 — ALGORITMO

Claude propuso una arquitectura candidata:

- Cuatro ejecuciones de Dijkstra.
- Identificación de aristas de caminos mínimos S→T.
- Construcción del DAG de caminos mínimos.
- Programación dinámica para aprovechar el pase.

No aceptes esa estrategia automáticamente.

Verifica que resuelve exactamente la semántica descubierta.

En particular:

- Los pesos son positivos y el DAG debe procesarse en orden válido.
- Los caminos mínimos alternativos deben tratarse correctamente.
- Las vías gratuitas utilizadas deben ser compatibles con las condiciones reales del pase.
- Debe considerarse la ruta U→V sin aprovechar el pase, cuando esté permitida.
- Deben contemplarse componentes desconectados.
- Dijkstra debe manejar pesos de hasta 4×10¹³.
- Las distancias válidas pueden aproximarse a 8×10¹⁸; no utilices un INF menor que una distancia válida posible.
- Protege las sumas intermedias de desbordamiento, utilizando comprobaciones previas o aritmética de 128 bits cuando corresponda.
- No dupliques innecesariamente estructuras grandes.

Busca una complejidad cercana a O((N+M)log N), siempre que las reglas la permitan.

No sacrifiques corrección para cumplir artificialmente esa complejidad.

## FASE A2.3 — PRUEBAS

Desarrolla una referencia exhaustiva independiente para grafos pequeños bajo las reglas confirmadas.

Prueba:

- Ejemplos oficiales.
- Resultados observados de caja negra.
- Grafos pequeños aleatorios.
- Grafos desconectados.
- S=T.
- U=V.
- Árboles.
- Ciclos.
- Múltiples caminos mínimos.
- Aristas paralelas.
- Bucles.
- Pesos mínimos y máximos.
- Grafos grandes dispersos.
- Grafos con 200,000 vértices y 400,000 aristas.

Comprueba por separado consumo de memoria, tiempo total y corrección.

---

# FASE GLOBAL — AUDITORÍA Y OPTIMIZACIÓN

Después de desarrollar cada solución:

### 1. Auditoría de corrección

Revisa independientemente:

- Interpretación real del problema.
- Correspondencia con la caja negra.
- Casos especiales.
- Validez de las transiciones.
- Invariantes del algoritmo.
- Corrección de la salida.
- Posibles desbordamientos.
- Condiciones de terminación.

Si detectas un problema, demuestra el fallo con un contraejemplo antes de modificar la implementación.

### 2. Pruebas diferenciales

Implementa referencias sencillas para entradas pequeñas y compara contra las soluciones optimizadas.

Establece pruebas aleatorias reproducibles mediante semillas fijas.

No inventes tasas de éxito. Informa el número exacto de pruebas ejecutadas, aprobadas y fallidas.

### 3. Evaluación de rendimiento

Compila en modo optimizado, por ejemplo:

`g++ -O2 -std=c++17`

Mide, cuando sea posible, tiempo de ejecución real y memoria máxima residente.

Objetivos:

- A1: menos de 24 segundos y 256 MB.
- A2: menos de 10 segundos y 128 MB.

Evita optimizaciones prematuras. Prioriza eliminar errores de complejidad y estructuras ineficientes.

Un benchmark local satisfactorio no garantiza aceptación en el juez oficial.

### 4. Eficiencia de las iteraciones

Organiza las tareas en una secuencia clara.

No repitas análisis ya confirmados sin nueva evidencia.

Cuando exista un fallo:

1. Reproduce el error.
2. Identifica su causa.
3. Corrige la parte mínima necesaria.
4. Ejecuta regresiones.
5. Actualiza la evidencia.

Prefiere conservar algoritmos demostrablemente correctos frente a reescrituras completas.

---

# FASE FINAL — ESTRUCTURA Y ENTREGA

El repositorio debe ser PRIVADO y llamarse exactamente como el equipo, usando guiones cuando corresponda.

Agregar a `DanielaaER` como colaboradora mediante GitHub.

Estructura obligatoria de Ronda 1:

```text
nombre-del-equipo/
└── R1/
    ├── ejercicio1/
    │   ├── codigo1.cpp
    │   └── conversacion1.md
    └── ejercicio2/
        ├── codigo2.cpp
        └── conversacion2.md
```

Los nombres de código deben comenzar con `codigo` y los de conversación con `conversacion`.

Cada conversación debe contener el historial COMPLETO y auténtico de las interacciones con IA correspondientes al ejercicio, incluyendo descubrimientos y pruebas de caja negra.

No sustituyas el historial real por un resumen generado ni fabriques conversaciones.

Si no puedes exportar automáticamente el historial completo, reporta esa limitación y deja pendiente su incorporación manual antes de considerar completa la entrega.

La bitácora adicional es opcional.

IMPORTANTE:

- El horario de entrega de cada ejercicio corresponde a su último commit.
- No modifiques una carpeta después de finalizar oficialmente su ejercicio.
- Mantén los experimentos temporales fuera de las carpetas oficiales.
- No realices un commit definitivo de un ejercicio sin verificar sus archivos y pruebas.
- Si el repositorio y las credenciales permiten completar las operaciones, sigue el procedimiento de Git establecido; si no, informa los pasos pendientes.
- Comprueba en GitHub que los archivos aparezcan.
- Verifica la privacidad del repositorio y la colaboradora requerida.
- La URL debe enviarse al enlace que indique el staff.
- No afirmes que la entrega fue completada sin confirmación efectiva.

---

# CRITERIOS DE ACEPTACIÓN

Una solución se considera técnicamente preparada solo cuando:

1. Las reglas ocultas relevantes están respaldadas por pruebas de caja negra, o las incertidumbres restantes están claramente documentadas.
2. Los ejemplos oficiales se superan.
3. La implementación coincide con una referencia independiente en los casos probados.
4. No se conocen contraejemplos sin resolver.
5. Se han evaluado los límites de tiempo y memoria.
6. Se ha auditado el manejo de enteros y casos límite.
7. El archivo final compila y ejecuta correctamente.
8. La conversación obligatoria está completa y es auténtica.
9. Los nombres y rutas de entrega son correctos.

Si alguna condición no se cumple, indica explícitamente el estado provisional y el riesgo.

# INFORME FINAL OBLIGATORIO

Al concluir, presenta una tabla breve:

| Aspecto | A1 | A2 |
|---|---|---|
| Reglas descubiertas | | |
| Algoritmo implementado | | |
| Complejidad temporal | | |
| Complejidad espacial | | |
| Pruebas aprobadas / ejecutadas | | |
| Tiempo medido | | |
| Memoria medida | | |
| Riesgo de WA/TLE/MLE | | |
| Estado de entrega | | |

Incluye únicamente información verificada o identificada explícitamente como estimación.

**ORDEN DE EJECUCIÓN:**

1. Inspecciona archivos y ejecutables disponibles.
2. Descubre reglas ocultas de A1.
3. Implementa, prueba y optimiza A1.
4. Descubre reglas ocultas de A2.
5. Implementa, prueba y optimiza A2.
6. Revisa ambas soluciones y la documentación.
7. Prepara la entrega oficial.

No te detengas después del análisis inicial. Ejecuta todas las fases técnicamente posibles sin solicitar confirmación en cada paso.

**OBJETIVO FINAL: conseguir dos soluciones correctas, eficientes, reproducibles y conformes con las reglas de la competencia.**