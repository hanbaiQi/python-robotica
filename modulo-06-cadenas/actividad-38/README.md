# Actividad 38 — Sobran espacios

- *Módulo*: 6 · Operaciones con cadenas
- *Fecha límite de entrega*: domingo 22 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

Un sensor a veces manda la lectura con espacios delante y detrás. `strip()` los quita. Los espacios de en medio se quedan.

## Objetivo

Limpiar los espacios de los extremos de una lectura.

## Lo que debes hacer

1. Crea `solucion/espacios.py`.
2. Declara `lectura = "  45 cm  "`.
3. Muestra `lectura`.
4. Muestra el resultado de `lectura.strip()`.
5. Ejecuta el programa y guarda la salida en `solucion/espacios-salida.txt`.

## Entregable

- `solucion/espacios.py`.
- `solucion/espacios-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Se muestra la lectura con los espacios | 25 % |
| Se muestra el resultado de `strip()` | 55 % |
| La salida está guardada en `espacios-salida.txt` | 20 % |

## Pista de cara al futuro

Después de `strip()`, la lectura se ve como `45 cm`. El espacio entre el número y `cm` sigue ahí.
