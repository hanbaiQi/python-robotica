# Actividad 40 — Separar palabras

- *Módulo*: 6 · Operaciones con cadenas
- *Fecha límite de entrega*: domingo 22 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

`split()` corta un texto por los espacios y devuelve una lista de palabras.

## Objetivo

Separar una frase del sensor en palabras y ver la lista.

## Lo que debes hacer

1. Crea `solucion/separar.py`.
2. Declara `frase = "sensor de distancia"`.
3. Guarda en `palabras` el resultado de `frase.split()`.
4. Muestra `palabras`.
5. Ejecuta el programa y guarda la salida en `solucion/separar-salida.txt`.

## Entregable

- `solucion/separar.py`.
- `solucion/separar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| La frase se separa con `split()` | 40 % |
| El resultado se guarda y se muestra | 40 % |
| La salida está guardada en `separar-salida.txt` | 20 % |

## Pista de cara al futuro

`split()` sin nada dentro corta por los espacios. El resultado es una lista, no un texto.
