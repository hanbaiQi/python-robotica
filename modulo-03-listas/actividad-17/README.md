# Actividad 17 — Cambiar una posición

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 8 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

Un sensor se sustituye por otro, pero la casilla sigue siendo la misma. Asignar con el índice cambia lo que hay en esa posición: no añade un elemento ni quita los demás.

## Objetivo

Sustituir el valor de una posición de la lista sin mover el resto y sin cambiar la longitud.

## Lo que debes hacer

1. Crea `solucion/asignar.py`.
2. Declara `sensores = ["ultrasonidos", "infrarrojos", "luz"]`.
3. Muestra la lista.
4. Cambia la posición 1 para que pase a ser `"presencia"`, con `sensores[1] = "presencia"`. No uses `append()`, `insert()` ni `remove()`. `"ultrasonidos"` y `"luz"` se quedan donde estaban, y la lista sigue teniendo tres elementos.
5. Vuelve a mostrar la lista.
6. Ejecuta el programa y guarda la salida en `solucion/asignar-salida.txt`.

## Entregable

- `solucion/asignar.py`.
- `solucion/asignar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Se muestra la lista antes de cambiar | 30 % |
| La posición 1 pasa a `"presencia"` con `sensores[1] = "presencia"` | 30 % |
| El resto no se mueve, la longitud no cambia y se vuelve a mostrar la lista | 20 % |
| La salida está guardada en `asignar-salida.txt` | 20 % |

## Pista de cara al futuro

El índice elige la casilla y el `=` sustituye lo que había, sin añadir ni quitar elementos.
