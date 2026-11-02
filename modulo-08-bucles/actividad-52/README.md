# Actividad 52 — Cinco pasos con for y range

- *Módulo*: 8 · Bucles
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: b) Se han utilizado estructuras de repetición.

## Contexto

A veces el robot no lleva la ruta en una lista: solo tiene que dar un número fijo de pasos. `range()` fabrica esa cuenta.

## Objetivo

Usar `for` con `range(1, 6)` para imprimir los cinco pasos del robot.

## Lo que debes hacer

1. Crea `solucion/pasos.py`.
2. Escribe `for paso in range(1, 6):`.
3. En cada vuelta, imprime `paso` con `print()`.
4. Ejecuta el programa y guarda la salida en `solucion/pasos-salida.txt`.

`range(1, 6)` empieza en 1 y llega hasta 5, no hasta 6. El 6 no entra. En la salida tienen que verse 1, 2, 3, 4 y 5, cada uno en su línea.

## Entregable

- `solucion/pasos.py`.
- `solucion/pasos-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| El `for` usa `range(1, 6)` | 35 % |
| Se imprimen los pasos 1, 2, 3, 4 y 5 | 35 % |
| El 6 no aparece en la salida | 15 % |
| La salida está guardada en `pasos-salida.txt` | 15 % |

## Pista de cara al futuro

Cada número de ese `range` es un paso que el robot da hacia delante.
