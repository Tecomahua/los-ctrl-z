# A1 — Tramos con mediana ≥ M

**Prompt & Code Challenge 2026 · Ronda 1 · Categoría Avanzada**

| Campo | Información |
|---|---|
| Equipo | **Los Ctrl + Z** |
| Repositorio privado propuesto | `los-ctrl-z` (validar denominación con el staff) |
| Ejercicio | A1 — Latencias y lecturas perdidas |
| Lenguaje de implementación previsto | C++17 |
| Estado | **Diseño candidato; reglas ocultas y código final pendientes de validación** |
| Juez | Entrada estándar (`stdin`), salida estándar (`stdout`) |

> **Alcance de este README:** documenta el problema, la propuesta algorítmica y el plan de verificación. **No sustituye** `codigo1.cpp` ni `conversacion1.md`. No se afirma que la caja negra haya sido ejecutada.

## 1. Descripción del problema

Dada una secuencia de `N` latencias, contar los tramos consecutivos `[i, j]` cuyo tamaño esté en `[L, R]` y cuya mediana sea **mayor o igual que `M`**. También se pide la suma de sus longitudes físicas `j - i + 1`. Una lectura `0` indica que se perdió; su tratamiento estadístico debe descubrirse con la caja negra oficial.

**Entrada:** primera línea `N L R M`; segunda línea, los `N` valores `a_i`.  
**Salida:** dos enteros separados por un espacio: `cantidad suma_de_longitudes`.

| Restricción | Valor |
|---|---:|
| `1 ≤ L ≤ R ≤ N` | `N ≤ 4 000 000` |
| `0 ≤ a_i ≤ 10⁹` | `1 ≤ M ≤ 10⁹` |
| Tiempo | **24 s** |
| Memoria | **256 MB** |

### Ejemplos oficiales

**Ejemplo 1 — Entrada**

```text
7 3 7 2
2 1 4 2 2 5 6
```

**Salida**

```text
15 65
```

**Ejemplo 2 — Entrada**

```text
9 5 9 3
4 2 5 5 2 4 6 1 6
```

**Salida**

```text
15 95
```

**Advertencia:** estos ejemplos no identifican las reglas ocultas; ambos contabilizan todos los tramos de las longitudes permitidas.

## 2. Reglas pendientes de descubrir

La documentación inicial de Claude **supone** mediana inferior para cantidades pares, exclusión de los ceros del cálculo de la mediana y tamaño medido por posiciones físicas. **Son hipótesis, no hechos confirmados.** También deben revisarse los tramos compuestos únicamente por ceros y el criterio de longitud acumulada.

La caja negra debe ejecutarse con entradas pequeñas e independientes:

| ID | Entrada: `N L R M` / `a_i` | Qué discrimina | Salida real |
|---|---|---|---|
| A1-01 | `2 2 2 3` / `1 5` | Mediana inferior frente a superior/promedio | Pendiente |
| A1-02 | `2 2 2 3` / `1 4` | Mediana superior frente a promedio, combinada con A1-01 | Pendiente |
| A1-03 | `3 1 1 3` / `0 5 0` | Tamaño físico frente a cantidad de lecturas válidas, condicionado a cómo se tratan los ceros | Pendiente |
| A1-04 | `3 3 3 5` / `5 0 0` | Ceros ignorados frente a ceros incluidos en la mediana | Pendiente |
| A1-05 | `3 2 3 5` / `0 0 0` | Validez de tramos sin lecturas disponibles | Pendiente |

Para las dos primeras pruebas, los resultados hipotéticos son:

- A1-01: `0 0` si se usa la mediana inferior; `1 2` si se usa la superior o el promedio.
- A1-02: `1 2` si se usa la superior; `0 0` si se usa la inferior o el promedio.

Estos resultados son **predicciones**, no respuestas observadas. Registrar los resultados efectivos y los experimentos adicionales en `conversacion1.md`.

## 3. Diseño algorítmico candidato

Claude propuso un enfoque **lineal**, sujeto a que la caja negra confirme las reglas supuestas:

1. Transformar cada valor en `+1` si `a_i ≥ M`, `-1` si `0 < a_i < M` y `0` si la lectura es perdida.
2. Construir las sumas prefijas `p`. Para un tramo `(i, j]`, estudiar `p[j] - p[i]`.
3. Bajo la hipótesis de ignorar ceros, comprobar una condición positiva para la **mediana inferior** y no negativa para la **superior**, excluyendo cuando corresponda los tramos sin lecturas válidas.
4. Mantener únicamente los prefijos de inicio en el intervalo `[j - R, j - L]`, con tablas de frecuencias y suma de índices.
5. Acumular simultáneamente el número de prefijos que cumplen la condición y `j × cantidad - suma_de_indices` para obtener la suma de longitudes.

Como los prefijos cambian a lo sumo una unidad por posición, la propuesta actualiza el umbral y los contadores en tiempo constante amortizado. **Si el juez usa la mediana promedio o tamaño por lecturas válidas, este razonamiento debe revisarse, no simplemente cambiar una constante.**

| Aspecto | Objetivo / estado |
|---|---|
| Tiempo teórico | **O(N)** bajo las hipótesis anteriores; por auditar |
| Memoria teórica | **O(N)**; arreglos principales ≈ 112 MB para `N = 4 000 000` |
| Acumulación | `unsigned long long` o tipo seguro equivalente |
| Riesgo principal | **WA** por semántica de mediana, ceros o tamaño no confirmada |

La suma máxima de longitudes, si todos los subarreglos son elegibles, es `N(N+1)(N+2)/6`; con `N = 4 000 000` supera `2⁶³−1`. También deben auditarse los productos intermedios.

## 4. Plan de verificación para Codex

- [ ] Ejecutar la caja negra; conservar cada entrada, salida y conclusión.
- [ ] Auditar los invariantes y extremos de la ventana `[j - R, j - L]`.
- [ ] Probar contra una referencia exhaustiva **independiente** en entradas pequeñas.
- [ ] Incluir casos con ceros, medianas pares/impares, `L=R`, `L=1`, `R=N` y extremos numéricos.
- [ ] Reproducir ambos ejemplos oficiales y conservar los registros de ejecución.
- [ ] Medir tiempo y pico de memoria con `N = 4 000 000` y patrones adversariales.
- [ ] Documentar discrepancias, contraejemplos, correcciones y estado final en `conversacion1.md`.

**Antecedentes reportados, no verificados aquí:** Claude informó 600 pruebas diferenciales sin discrepancias y una medición de 0.13 s con aproximadamente 110 MB. No se aportaron registros reproducibles ni resultados de la caja negra. **No utilizar esas cifras como evidencia de aceptación oficial.**

## 5. Compilación y ejecución

Desde la raíz del repositorio, **una vez que Codex haya creado `codigo1.cpp`**:

```bash
g++ -O2 -std=c++17 -Wall -Wextra R1/ejercicio1/codigo1.cpp -o a1
printf '7 3 7 2\n2 1 4 2 2 5 6\n' | ./a1
# Salida oficial esperada: 15 65
```

La solución final debe escribir **solo** los dos enteros requeridos. El rendimiento real dependerá del entorno del juez.

## 6. IA utilizada y trazabilidad

| Herramienta | Contribución en la preparación | Estado |
|---|---|---|
| **Claude AI** | Algoritmo lineal candidato, código C++ preliminar y propuestas de caja negra | Por auditar |
| **Microsoft Copilot** | Desglose de requisitos, casos límite y proceso de validación | Insumo metodológico |
| **ChatGPT (GPT-6)** | Comparación crítica, ingeniería de prompts y consolidación documental | Documento preparado |
| **OpenAI Codex** | Implementación final, pruebas y optimización | **Pendiente** |

La participación de una IA **no implica que sus resultados hayan sido verificados**. El historial completo, auténtico y exportado de las conversaciones utilizadas para este ejercicio se deberá adjuntar por separado como `conversacion1.md` (o extensión admitida por el staff). Un README o una síntesis no reemplazan dicho historial.

## 7. Entrega oficial

Ruta exigida: `R1/ejercicio1/`.

```text
R1/ejercicio1/
├── codigo1.cpp          # Obligatorio; un único archivo fuente
├── conversacion1.md     # Obligatorio; historial íntegro, con pruebas de caja negra
└── README.md            # Documentación complementaria
```

- [ ] Código final compilable, sin dependencias externas ni salida de depuración.
- [ ] Conversación completa, con los resultados reales de caja negra y sus descubrimientos.
- [ ] Repositorio **privado** del equipo **Los Ctrl + Z**, con `DanielaaER` como colaboradora.
- [ ] Archivos verificados en GitHub y URL remitida según indique el staff.
- [ ] No volver a modificar esta carpeta después del commit final: **cuenta la hora del último commit que la afecte**.

**Estado de entrega: pendiente.** El código y el historial obligatorio se incorporarán y validarán antes del envío.
