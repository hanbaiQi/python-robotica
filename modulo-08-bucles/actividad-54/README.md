# Actividad 54 — Parar la ruta con for y break

- *Módulo*: 8 · Bucles
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: b) Se han utilizado estructuras de repetición. c) Se han reconocido las posibilidades de las sentencias de salto.

## Contexto

La lista de órdenes sigue después de `"parar"`, pero el robot no debe obedecer lo que va detrás. `break` corta el `for` en esa vuelta.

## Objetivo

Recorrer las órdenes con `for`, imprimirlas y salir del bucle con `break` cuando la orden sea `"parar"`.

## Lo que debes hacer

1. Crea `solucion/detener.py`.
2. Declara `ordenes = ["adelante", "izquierda", "parar", "derecha", "adelante"]`.
3. Recorre la lista con `for orden in ordenes:`.
4. En cada vuelta, imprime `orden`.
5. Si `orden == "parar"`, ejecuta `break`.
6. Ejecuta el programa y guarda la salida en `solucion/detener-salida.txt`.

`"parar"` sí se imprime: el `break` va después del `print()`. `"derecha"` y el `"adelante"` que van detrás no salen.

## Entregable

- `solucion/detener.py`.
- `solucion/detener-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| El `for` imprime cada orden que llega a leer | 25 % |
| `break` se ejecuta cuando la orden es `"parar"` | 30 % |
| `"derecha"` y el `"adelante"` posteriores no se imprimen | 30 % |
| La salida está guardada en `detener-salida.txt` | 15 % |

## Pista de cara al futuro

Cuando la orden es parar, el robot deja de leer el resto de la lista.
