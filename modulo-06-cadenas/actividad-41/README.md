# Actividad 41 — Unir con guiones

- *Módulo*: 6 · Operaciones con cadenas
- *Fecha límite de entrega*: domingo 22 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

`join` hace el camino contrario a `split`. Parte de una lista de palabras y las pega en un solo texto, con el separador que elijas.

## Objetivo

Unir tres palabras con guiones.

## Lo que debes hacer

1. Crea `solucion/unir.py`.
2. Declara `palabras = ["sensor", "de", "distancia"]`.
3. Guarda en `unido` el resultado de `"-".join(palabras)`.
4. Muestra `unido`.
5. Ejecuta el programa y guarda la salida en `solucion/unir-salida.txt`.

## Entregable

- `solucion/unir.py`.
- `solucion/unir-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Las palabras se unen con `"-".join(palabras)` | 50 % |
| Se muestra el texto unido | 30 % |
| La salida está guardada en `unir-salida.txt` | 20 % |

## Pista de cara al futuro

El texto que va delante de `.join` es el pegamento. Aquí es un guion, y queda entre palabra y palabra.
