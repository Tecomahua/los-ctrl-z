# A2 — Pase express en caminos mínimos

**Prompt & Code Challenge 2026 · Ronda 1 · Categoría Avanzada**

| Campo | Información |
|---|---|
| Equipo | **Los Ctrl + Z** |
| Repositorio privado propuesto | `los-ctrl-z` (validar denominación con el staff) |
| Ejercicio | A2 — Grafo ponderado con pase express |
| Lenguaje de implementación previsto | C++17 |
| Estado | **Diseño candidato; condiciones del pase y código final pendientes de validación** |
| Juez | Entrada estándar (`stdin`), salida estándar (`stdout`) |

> **Alcance de este README:** documenta el problema, la propuesta algorítmica y el plan de verificación. **No sustituye** `codigo2.cpp` ni `conversacion2.md`. No se afirma que la caja negra haya sido ejecutada.

## 1. Descripción del problema

Una ciudad cuenta con `N` estaciones y `M` vías **bidireccionales** de costo positivo. El viaje habitual va de `S` a `T`. El pase express permite elegir **uno** de los caminos de costo mínimo de `S` a `T` y obtener gratuidad en sus vías, según condiciones de uso **no especificadas**. Se pide el costo mínimo para viajar de `U` a `V`, o `-1` si no existe una ruta válida.

**Entrada:** `N M`; luego `S T U V`; finalmente `M` líneas `a b w`.  
**Salida:** un entero con el costo mínimo o `-1`.

| Restricción | Valor |
|---|---:|
| Estaciones | `1 ≤ N ≤ 200 000` |
| Vías | `0 ≤ M ≤ 400 000` |
| Peso de cada vía | `1 ≤ w ≤ 4 × 10¹³` |
| Características | Se permiten vías paralelas y bucles |
| Tiempo | **10 s** |
| Memoria | **128 MB** |

### Ejemplos oficiales

**Ejemplo 1 — Entrada**

```text
4 5
4 2 3 2
4 1 7
2 4 8
1 1 3
3 4 9
4 2 7
```

**Salida**

```text
9
```

**Ejemplo 2 — Entrada**

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

**Salida**

```text
2
```

Los ejemplos no determinan por sí solos las condiciones reales del pase.

## 2. Reglas pendientes de descubrir

La propuesta inicial de Claude **supone** que el pase se puede utilizar en ambos sentidos y sobre cualquier subtramo de **un único** camino mínimo seleccionado. Nada de esto está confirmado por la caja negra.

Deben investigarse además: elección entre caminos mínimos alternativos, posible reutilización de vías, `S=T`, desconexión entre `S` y `T`, vías paralelas y bucles. La presencia de una arista en **algún** camino mínimo no implica que todas esas aristas puedan usarse gratis conjuntamente.

Pruebas pequeñas, cada una en una ejecución independiente:

| ID | Entrada resumida | Qué discrimina | Salida real |
|---|---|---|---|
| A2-01 | `2 1` / `1 2 2 1` / `1 2 5` | Pase en sentido inverso: `0` frente a `5`, bajo hipótesis básicas | Pendiente |
| A2-02 | `3 2` / `1 3 2 3` / `1 2 1` / `2 3 1` | Uso de subtramo: `0` frente a `1`, bajo hipótesis básicas | Pendiente |
| A2-03 | `4 4` / `1 4 2 3` / `1 2 1`; `2 4 1`; `1 3 1`; `3 4 1` | Solo un camino seleccionado frente a unión gratuita de varios | Pendiente |
| A2-04 | `4 2` / `1 2 3 4` / `1 3 2`; `3 4 2` | Efecto de no existir camino `S → T` | Pendiente |

**Interpretaciones ilustrativas:** A2-03 puede producir `1` si se elige un solo camino gratuito, o `0` si se permite liberar simultáneamente las vías de ambos caminos. A2-04 puede producir `2` si viajar sin pase sigue permitido, u otro resultado si se exige la existencia del camino habitual. Son **predicciones condicionadas**, no salidas de la caja.

Registrar todas las pruebas, las hipótesis descartadas y cualquier incertidumbre residual en `conversacion2.md`.

## 3. Diseño algorítmico candidato

Claude propuso **cuatro ejecuciones de Dijkstra** desde `S`, `T`, `U` y `V`, seguidas de un procesamiento sobre el **DAG de caminos mínimos** de `S` a `T`:

1. Calcular las distancias `dS`, `dT`, `dU` y `dV` mediante Dijkstra.
2. Identificar los vértices y aristas compatibles con algún camino mínimo de `S` a `T` mediante condiciones de distancias, **sin tratar su unión como un pase gratuito global**.
3. Orientar las aristas del subgrafo de caminos mínimos desde menor a mayor distancia respecto a `S`. Como los pesos son estrictamente positivos, la orientación es acíclica.
4. Procesar el DAG en orden válido y mantener el mejor costo para alcanzar un punto de entrada al tramo gratuito.
5. Combinar los costos exteriores con el beneficio de un subcamino gratuito y evaluar, si la regla lo permite, ambas orientaciones.
6. Comparar con el trayecto ordinario `U → V` cuando corresponda y decidir si debe imprimirse `-1`.

**Condición de corrección:** la programación dinámica debe garantizar que las transiciones utilizadas sean compatibles con **un mismo camino mínimo elegible** y con las reglas de dirección, continuidad y consumo del pase. No basta con identificar aristas que pertenecen individualmente a caminos mínimos.

| Aspecto | Objetivo / estado |
|---|---|
| Tiempo teórico | **O((N + M) log N)**, sujeto a la semántica del pase |
| Memoria teórica | **O(N + M)**; verificar el pico real frente a 128 MB |
| Distancias | Hasta `(N - 1) × 4 × 10¹³ ≈ 8 × 10¹⁸` en un camino simple |
| Precisión numérica | Usar 64 bits para distancias finitas cuando baste y `__int128` o sumas protegidas para expresiones intermedias |
| Riesgo principal | **WA** por mezclar caminos incompatibles o asumir reglas de uso no verificadas |

Evitar un valor `INF` menor que una distancia válida. Revisar explícitamente sumas con distancias no alcanzables, caminos alternativos, bucles y vías paralelas. No afirmar que no existen desbordamientos sin demostrarlo.

## 4. Plan de verificación para Codex

- [ ] Ejecutar la caja negra para dirección, uso parcial y elección del camino; añadir pruebas discriminantes si es necesario.
- [ ] Revisar la lógica del DAG y demostrar que el aprovechamiento gratuito es legal.
- [ ] Contrastar con una referencia exhaustiva **independiente** para grafos pequeños.
- [ ] Incluir `M=0`, `S=T`, `U=V`, componentes desconectados, ciclos, rutas empatadas, bucles y aristas paralelas.
- [ ] Probar pesos máximos y revisar todas las sumas de distancias e infinitos.
- [ ] Reproducir ambos ejemplos oficiales.
- [ ] Medir tiempo y pico de memoria con hasta `N=200 000`, `M=400 000` y grafos adversariales.
- [ ] Documentar contraejemplos, correcciones y evidencia reproducible en `conversacion2.md`.

**Antecedentes reportados, no verificados aquí:** Claude informó 500 pruebas diferenciales sin discrepancias y una medición de 0.73 s con el tamaño máximo. No se aportaron registros reproducibles ni resultados de la caja negra. **No presentar esas cifras como validación oficial.**

## 5. Compilación y ejecución

Desde la raíz del repositorio, **una vez que Codex haya creado `codigo2.cpp`**:

```bash
g++ -O2 -std=c++17 -Wall -Wextra R1/ejercicio2/codigo2.cpp -o a2
printf '4 5\n4 2 3 2\n4 1 7\n2 4 8\n1 1 3\n3 4 9\n4 2 7\n' | ./a2
# Salida oficial esperada: 9
```

La solución final debe producir exactamente un entero y ningún mensaje adicional en `stdout`.

## 6. IA utilizada y trazabilidad

| Herramienta | Contribución en la preparación | Estado |
|---|---|---|
| **Claude AI** | Cuatro Dijkstra, propuesta de DAG/DP, pruebas sugeridas y código C++ preliminar reportado | Por auditar |
| **Microsoft Copilot** | Análisis de hipótesis, matriz de escenarios y estrategia de validación | Insumo metodológico |
| **ChatGPT (GPT-6)** | Comparación crítica, ingeniería de prompts y consolidación documental | Documento preparado |
| **OpenAI Codex** | Implementación final, pruebas y optimización | **Pendiente** |

La participación de una IA **no implica que sus resultados hayan sido verificados**. La conversación completa y auténtica de este ejercicio, con prompts y experimentos, debe exportarse por separado como `conversacion2.md` (o extensión admitida por el staff). No sustituirla por una síntesis del README.

## 7. Entrega oficial

Ruta exigida: `R1/ejercicio2/`.

```text
R1/ejercicio2/
├── codigo2.cpp          # Obligatorio; un único archivo fuente
├── conversacion2.md     # Obligatorio; historial íntegro, con pruebas de caja negra
└── README.md            # Documentación complementaria
```

- [ ] Código final compilable, sin dependencias externas ni salida de depuración.
- [ ] Conversación completa, incluyendo caja negra y decisiones técnicas.
- [ ] Repositorio **privado** del equipo **Los Ctrl + Z**, con `DanielaaER` como colaboradora.
- [ ] Archivos verificados en GitHub y URL remitida según indique el staff.
- [ ] No volver a modificar esta carpeta después del commit final: **cuenta la hora del último commit que la afecte**.

**Estado de entrega: pendiente.** El código y el historial obligatorio se incorporarán y validarán antes del envío.
