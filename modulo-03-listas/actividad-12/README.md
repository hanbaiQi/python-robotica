# Actividad 12 — Colócalo en su sitio

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 1 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

A veces el dato nuevo no va al final. `insert(posicion, valor)` lo coloca en ese índice y desplaza hacia la derecha todo lo que había a partir de ahí.

## Objetivo

Insertar un valor en una posición concreta de una lista.

## Lo que debes hacer

1. Crea `solucion/insertar.py`.
2. Declara `ruta = ["adelante", "adelante", "derecha", "parar"]`.
3. Muestra la ruta.
4. Inserta `"izquierda"` en la posición 2 con `insert(2, "izquierda")`. El paso de la posición 2 pasa a ser `"izquierda"`, y `"derecha"` y `"parar"` se corren un puesto.
5. Vuelve a mostrar la ruta.
6. Ejecuta el programa y guarda la salida en `solucion/insertar-salida.txt`.

## Entregable

- `solucion/insertar.py`.
- `solucion/insertar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Se muestra la ruta antes de insertar | 25 % |
| `"izquierda"` queda en el índice 2 mediante `insert()` | 35 % |
| Se muestra la ruta después, con el resto desplazado | 20 % |
| La salida está guardada en `insertar-salida.txt` | 20 % |

## Pista de cara al futuro

La posición de `insert()` es un índice: 0 es el principio. Si insertas en el 0, todo lo demás se corre un puesto hacia la derecha.
