# Los Ctrl + Z — Prompt & Code Challenge 2026

Repositorio del equipo para las rondas 1 y 2. La Ronda 2 se entrega en
`R2/ejercicio1/`, en el mismo repositorio de la Ronda 1.

## Ronda 1

Se conservan las bitácoras parciales de prompts, las propuestas técnicas recibidas
y el avance de los dos ejercicios de la Ronda 1.

| Ejercicio | Bitácora de prompts y avance | Código provisional | Fuente técnica recibida |
|---|---|---|---|
| A1 — Latencias y medianas | [R1/ejercicio1/README.md](R1/ejercicio1/README.md) | [codigo1.cpp](R1/ejercicio1/codigo1.cpp) | [README de A1](fuentes/README_A1_recibido.md) |
| A2 — Pase express | [R1/ejercicio2/README.md](R1/ejercicio2/README.md) | [codigo2.cpp](R1/ejercicio2/codigo2.cpp) | [README de A2](fuentes/README_A2_recibido.md) |

El [prompt maestro de Ronda 1](PROMPT_MAESTRO.md) se conserva como fuente textual
única para ambos ejercicios. `pruebas_locales.js` y `generar_benchmarks.js` permiten
reproducir sus pruebas tras compilar los archivos C++17.

## Ronda 2

| Ejercicio | Código C++17 | Conversación real | Informe y bitácora |
|---|---|---|---|
| AF — Transmisiones masivas | [codigo1.cpp](R2/ejercicio1/codigo1.cpp) | [conversacion1.md](R2/ejercicio1/conversacion1.md) | [README del ejercicio](R2/ejercicio1/README.md) |

```text
R2/
├── ejercicio1/
│   ├── codigo1.cpp
│   ├── conversacion1.md
│   └── README.md
└── pruebas/
    ├── README.md
    ├── diferencial.py
    ├── estres.py
    └── ... registros, resultados y utilidades
```

Validación ejecutada en Windows: dos ejemplos oficiales, 224 casos dirigidos y
3,000 entradas aleatorias sin discrepancias con el oráculo. Diez escenarios de
cinco millones de líneas dieron las salidas esperadas. Máximo observado de la
solución en la tanda de estrés: **1.023 s y 43.7 MiB residentes**. Son mediciones del
equipo local; Linux no pudo ejecutarse por un fallo del servicio WSL.

Las cuatro reglas ocultas, la justificación del algoritmo y las limitaciones de
la evidencia están en el informe. Las [pruebas reproducibles](R2/pruebas/README.md)
conservan entradas y salidas reales; no incluyen ejecutables ni archivos masivos.
La conversación es una exportación del registro real con un corte explícito.

La actualización del **5 de noviembre de 2026** sigue la estructura de entrega
indicada por el usuario. Los nuevos commits usan el mensaje **`R2`**, siguiendo la
convención `R1` del historial. La hora de entrega depende del último commit que
afecte a `R2/ejercicio1/`, según las indicaciones de la ronda.

La entrega se propone en el [pull request #1 — R2: Transmisiones masivas (AF)](https://github.com/Tecomahua/los-ctrl-z/pull/1),
desde `codex/r2-transmisiones-masivas` hacia `main`. En la comprobación posterior
a su creación GitHub lo marcó sin conflictos; no había ejecuciones de CI.

Este README y el del ejercicio se actualizarán con los hallazgos y verificaciones
que se produzcan en la conversación. El registro conversacional conserva los
mensajes originales; los README documentan los resultados técnicos observables.
