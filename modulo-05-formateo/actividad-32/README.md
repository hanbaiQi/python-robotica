# Actividad 32 — Sin salto de línea

- *Módulo*: 5 · Formateo de cadenas
- *Fecha límite de entrega*: domingo 22 de noviembre de 2026, 23:59
- *RA 5*: b) Se han aplicado formatos en la visualización de la información.

## Contexto

Cada `print` termina en un salto de línea. `end=""` lo quita, y el siguiente `print` sigue en la misma línea.

## Objetivo

Escribir una etiqueta y un valor en la misma línea usando dos `print`.

## Lo que debes hacer

1. Crea `solucion/linea.py`.
2. El primer `print` muestra `"Distancia:"` y termina con `end=" "`.
3. El segundo `print` muestra `45`.
4. Los dos tienen que quedar en la misma línea.
5. Ejecuta el programa y guarda la salida en `solucion/linea-salida.txt`.

## Entregable

- `solucion/linea.py`.
- `solucion/linea-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| El primer `print` usa `end=" "` | 40 % |
| La etiqueta y el 45 quedan en la misma línea | 40 % |
| La salida está guardada en `linea-salida.txt` | 20 % |

## Pista de cara al futuro

`end` es lo que se escribe al terminar ese `print`. Un espacio deja la línea abierta para el número.
