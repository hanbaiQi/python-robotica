# Actividad 14 — De cerca a lejos

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 8 de noviembre de 2026, 23:59
- *RA 1*: d) Se han identificado los distintos tipos de variables y la utilidad específica de cada uno. e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

El robot mide distancias en centímetros. `sorted()` devuelve una lista nueva, ordenada de menor a mayor, y deja la original como estaba. El primer valor de esa lista nueva es el más cercano; el último, el más lejano.

## Objetivo

Ordenar una lista de números y leer el menor y el mayor por su posición.

## Lo que debes hacer

1. Crea `solucion/distancias.py`.
2. Declara `distancias = [40, 12, 80, 25]`. Son centímetros.
3. Guarda el resultado de `sorted(distancias)` en una variable llamada `ordenadas`.
4. Muestra `distancias` y `ordenadas` en líneas distintas. La primera tiene que seguir siendo `[40, 12, 80, 25]`.
5. Muestra el más cercano, `ordenadas[0]`, y el más lejano, `ordenadas[-1]`.
6. Ejecuta el programa y guarda la salida en `solucion/distancias-salida.txt`.

El orden sale de `sorted()` y las dos distancias, de los índices.

## Entregable

- `solucion/distancias.py`.
- `solucion/distancias-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| `ordenadas` se obtiene con `sorted()` y la lista original no cambia | 40 % |
| Se muestran la lista original y la ordenada | 20 % |
| Se muestran el más cercano y el más lejano con los índices 0 y -1 | 20 % |
| La salida está guardada en `distancias-salida.txt` | 20 % |

## Pista de cara al futuro

`sorted()` te da otra lista. Si imprimes las dos, ves la medida tal como llegó y la misma medida ya ordenada.
