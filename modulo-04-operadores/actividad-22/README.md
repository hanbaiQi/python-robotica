# Actividad 22 — Resto y potencia

- *Módulo*: 4 · Operadores básicos
- *Fecha límite de entrega*: domingo 15 de noviembre de 2026, 23:59
- *RA 1*: g) Se han clasificado, reconocido y utilizado en expresiones los operadores del lenguaje.

## Contexto

`%` dice lo que sobra al repartir. `**` eleva un número a una potencia. El robot los usa para el resto de una carga y para una potencia sencilla.

## Objetivo

Usar el resto y la potencia, y mostrar los dos resultados.

## Lo que debes hacer

1. Crea `solucion/resto.py`.
2. Declara `carga = 100` y `tramo = 30`. Guarda en `sobra` el resultado de `carga % tramo`.
3. Declara `voltaje = 3`. Guarda en `potencia` el resultado de `voltaje ** 2`.
4. Muestra `sobra` y `potencia`, cada uno en su línea.
5. Ejecuta el programa y guarda la salida en `solucion/resto-salida.txt`.

## Entregable

- `solucion/resto.py`.
- `solucion/resto-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| `sobra` se calcula con `%` | 30 % |
| `potencia` se calcula con `**` | 30 % |
| Se muestran los dos resultados | 20 % |
| La salida está guardada en `resto-salida.txt` | 20 % |

## Pista de cara al futuro

100 entre 30 cabe 3 veces y sobran 10. `3 ** 2` es 3 elevado a 2.
