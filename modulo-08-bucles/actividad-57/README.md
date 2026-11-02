# Actividad 57 — Salta el paso 3 con while y continue

- *Módulo*: 8 · Bucles
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: b) Se han utilizado estructuras de repetición. c) Se han reconocido las posibilidades de las sentencias de salto.

## Contexto

El robot numera sus pasos del 1 al 6, pero el paso 3 es un hueco del recorrido y no lo anuncia. `continue` salta el resto de esa vuelta y vuelve a la condición del `while`.

## Objetivo

Contar hasta 6 con un `while` y saltar la impresión del paso 3 con `continue`.

## Lo que debes hacer

1. Crea `solucion/saltar.py`.
2. Empieza con `paso = 0`.
3. Escribe `while paso < 6:`.
4. Dentro del `while`, suma 1 a `paso`.
5. Si `paso == 3`, ejecuta `continue`.
6. Si no es 3, imprime `paso`.
7. Ejecuta el programa y guarda la salida en `solucion/saltar-salida.txt`.

La suma va antes del `if`. Cuando `paso` vale 3, `continue` vuelve a la condición del `while` y no llega al `print()`. El 3 se ha contado, pero no se imprime. Por eso la salida es 1, 2, 4, 5 y 6.

## Entregable

- `solucion/saltar.py`.
- `solucion/saltar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| `paso` empieza en 0 y la condición del `while` es `paso < 6` | 20 % |
| En cada vuelta se suma 1 antes del `if` | 20 % |
| Cuando `paso` es 3, `continue` evita imprimirlo | 30 % |
| Se imprimen 1, 2, 4, 5 y 6 | 20 % |
| La salida está guardada en `saltar-salida.txt` | 10 % |

## Pista de cara al futuro

El paso 3 es un hueco del recorrido: el robot lo cuenta y sigue, pero no lo anuncia.
