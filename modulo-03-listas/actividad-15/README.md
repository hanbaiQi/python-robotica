# Actividad 15 — Un trozo del recorrido

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 8 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

A veces el robot no necesita toda la ruta, solo un tramo. `ruta[ini:fin]` devuelve una lista nueva con los elementos desde el índice `ini` hasta justo antes de `fin`. El índice `fin` no entra.

## Objetivo

Cortar una lista en dos tramos y comprobar qué índices entran en el corte.

## Lo que debes hacer

1. Crea `solucion/cortar.py`.
2. Declara `ruta = ["adelante", "izquierda", "adelante", "derecha", "adelante", "parar"]`. Son seis pasos.
3. Muestra la ruta completa.
4. Muestra el tramo `ruta[0:3]`.
5. Muestra el tramo `ruta[2:5]`.
6. Ejecuta el programa y guarda la salida en `solucion/cortar-salida.txt`.

El índice final del corte no entra.

## Entregable

- `solucion/cortar.py`.
- `solucion/cortar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| La ruta tiene los seis pasos en el orden pedido | 25 % |
| Se muestran los cortes `ruta[0:3]` y `ruta[2:5]` | 50 % |
| La salida está guardada en `cortar-salida.txt` | 25 % |

## Pista de cara al futuro

El corte es otra lista, más corta, y `ruta` sigue entera. De 0 a 3 salen tres pasos, porque el 3 se queda fuera.
