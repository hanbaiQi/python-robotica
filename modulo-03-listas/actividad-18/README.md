# Actividad 18 — Todos los métodos, con números

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 8 de noviembre de 2026, 23:59
- *RA 1*: d) Se han identificado los distintos tipos de variables y la utilidad específica de cada uno. e) Se ha modificado el código de un programa para crear y utilizar variables.
- *RA 2*: b) Se han escrito programas simples.

## Contexto

Un sensor del robot va dejando distancias en centímetros, todas en una sola lista de números. Este programa junta lo anterior: crear la lista, leer su longitud y sus extremos, añadir, insertar, cambiar una casilla, quitar un valor, ordenar y cortar.

## Objetivo

Usar, en un solo programa y en el orden indicado, los métodos de lista de las actividades anteriores, esta vez con números.

## Lo que debes hacer

1. Crea `solucion/numeros.py`.
2. Declara `medidas = [40, 12, 80, 25]`. Muestra la lista, `len(medidas)`, `medidas[0]` y `medidas[-1]`.
3. Añade `5` al final con `append(5)`. Muestra la lista.
4. Inserta `30` en la posición 1 con `insert(1, 30)`. Muestra la lista.
5. Asigna la posición 0, que ya existe, con `medidas[0] = 15`. La longitud no cambia. Muestra la lista.
6. Quita `80` con `remove(80)`. Ese valor sigue en la lista después de los pasos anteriores. Muestra la lista.
7. Guarda `sorted(medidas)` en `ordenadas`. Muestra `medidas`, que no cambia, y `ordenadas`. El más cercano es `ordenadas[0]` y el más lejano, `ordenadas[-1]`: muéstralos.
8. Muestra el corte `medidas[1:4]`.
9. Ejecuta el programa y guarda la salida en `solucion/numeros-salida.txt`.

Cada impresión se hace con `print()`. En el corte, el índice final no entra.

## Entregable

- `solucion/numeros.py`.
- `solucion/numeros-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Se muestran la lista inicial, `len(medidas)`, el índice 0 y el índice -1 | 15 % |
| `5` se añade al final con `append()` y se muestra la lista | 10 % |
| `30` queda en el índice 1 con `insert()` y se muestra la lista | 15 % |
| La posición 0 pasa a `15` y la longitud no cambia | 15 % |
| `80` se quita con `remove()` y se muestra la lista | 15 % |
| `ordenadas` sale de `sorted()`, `medidas` no cambia, y se muestran el más cercano y el más lejano | 15 % |
| Se muestra el corte `medidas[1:4]` | 10 % |
| La salida está guardada en `numeros-salida.txt` | 5 % |

## Pista de cara al futuro

Con números se usan los mismos métodos que con los nombres de los sensores. `sorted()` ordena de menor a mayor y no toca la lista original.
