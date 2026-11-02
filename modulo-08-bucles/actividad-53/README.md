# Actividad 53 — Cuenta los giros con for

- *Módulo*: 8 · Bucles
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: b) Se han utilizado estructuras de repetición.

## Contexto

En una ruta hay pasos rectos y giros. El robot necesita saber cuántas veces ha girado a la izquierda y cuántas a la derecha. Un contador es una variable que empieza en 0 y suma 1 cada vez que aparece ese giro.

## Objetivo

Recorrer una lista de órdenes con `for` y contar, con un `if` dentro del bucle, las veces que gira a cada lado.

## Lo que debes hacer

1. Crea `solucion/giros.py`.
2. Declara `ordenes = ["adelante", "izquierda", "adelante", "derecha", "izquierda", "derecha", "adelante", "izquierda"]`.
3. Crea dos contadores a 0: `izquierdas` y `derechas`.
4. Recorre la lista con `for orden in ordenes:`.
5. Dentro del `for`, si `orden == "izquierda"`, suma 1 a `izquierdas`. Si `orden == "derecha"`, suma 1 a `derechas`.
6. Cuando el `for` termine, imprime `izquierdas` y, en la línea siguiente, `derechas`.
7. Ejecuta el programa y guarda la salida en `solucion/giros-salida.txt`.

En esta ruta hay tres `"izquierda"` y dos `"derecha"`. La salida son las líneas `3` y `2`.

## Entregable

- `solucion/giros.py`.
- `solucion/giros-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| `ordenes` es la lista del enunciado | 20 % |
| `izquierdas` y `derechas` empiezan en 0 | 15 % |
| El `if` está dentro del `for` y solo suma cuando la orden es ese giro | 30 % |
| Al final se imprimen 3 y 2, en ese orden | 20 % |
| La salida está guardada en `giros-salida.txt` | 15 % |

## Pista de cara al futuro

Contar los giros le dice al robot cuántas veces ha torcido a cada lado.
