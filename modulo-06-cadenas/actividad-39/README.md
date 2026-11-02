# Actividad 39 — Cambiar una palabra

- *Módulo*: 6 · Operaciones con cadenas
- *Fecha límite de entrega*: domingo 22 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

`replace` cambia un trozo de texto por otro. Devuelve un texto nuevo. La variable original se queda como estaba si no guardas el resultado.

## Objetivo

Cambiar la orden `"adelante"` por `"atras"`.

## Lo que debes hacer

1. Crea `solucion/cambiar.py`.
2. Declara `orden = "adelante"`.
3. Guarda en `nueva` el resultado de `orden.replace("adelante", "atras")`.
4. Muestra `orden` y `nueva`, cada una en su línea.
5. Ejecuta el programa y guarda la salida en `solucion/cambiar-salida.txt`.

## Entregable

- `solucion/cambiar.py`.
- `solucion/cambiar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| El cambio se hace con `replace("adelante", "atras")` | 40 % |
| Se muestran la orden original y la nueva | 40 % |
| La salida está guardada en `cambiar-salida.txt` | 20 % |

## Pista de cara al futuro

El primer texto de `replace` es el que buscas. El segundo es el que lo sustituye.
