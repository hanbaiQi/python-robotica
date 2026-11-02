# Actividad 51 — Recorre las órdenes con for

- *Módulo*: 8 · Bucles
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: b) Se han utilizado estructuras de repetición.

## Contexto

El robot guarda la ruta en una lista de órdenes. Un `for` las lee de la primera a la última, una por vuelta, y las muestra en ese orden.

## Objetivo

Recorrer una lista con `for` e imprimir cada orden en su propia línea.

## Lo que debes hacer

1. Crea `solucion/ordenes.py`.
2. Declara `ordenes = ["adelante", "izquierda", "adelante", "derecha", "parar"]`.
3. Recorre la lista con `for orden in ordenes:`.
4. En cada vuelta, imprime `orden` con `print()`. Cada orden queda en su línea.
5. Ejecuta el programa y guarda la salida en `solucion/ordenes-salida.txt`.

## Entregable

- `solucion/ordenes.py`.
- `solucion/ordenes-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| `ordenes` tiene las cinco órdenes en el orden del enunciado | 25 % |
| Un `for` recorre la lista | 35 % |
| Cada orden se imprime en su línea, de la primera a la última | 25 % |
| La salida está guardada en `ordenes-salida.txt` | 15 % |

## Pista de cara al futuro

El `for` lee las órdenes del robot en el orden de la lista, una por vuelta.
