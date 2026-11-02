# Actividad 42 — La frase del sensor

- *Módulo*: 6 · Operaciones con cadenas
- *Fecha límite de entrega*: domingo 22 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

Una lectura llega con espacios de sobra. Hay que limpiarla, pasarla a mayúsculas, contar sus caracteres, partirla en palabras y volver a unir esas palabras con guiones.

## Objetivo

Encadenar `strip`, `upper`, `len`, `split` y `join` sobre la misma frase.

## Lo que debes hacer

1. Crea `solucion/frase.py`.
2. Declara `lectura = "  el sensor mide distancia  "`.
3. Guarda en `limpia` el resultado de `lectura.strip()`.
4. Guarda en `mayusculas` el resultado de `limpia.upper()`.
5. Muestra `mayusculas`.
6. Muestra `len(mayusculas)`.
7. Guarda en `palabras` el resultado de `mayusculas.split()`.
8. Muestra el resultado de `"-".join(palabras)`.
9. Ejecuta el programa y guarda la salida en `solucion/frase-salida.txt`.

## Entregable

- `solucion/frase.py`.
- `solucion/frase-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| La frase se limpia con `strip` y pasa a mayúsculas con `upper` | 30 % |
| Se muestra la longitud con `len` | 20 % |
| Las palabras se separan con `split` y se unen con `"-".join` | 30 % |
| La salida está guardada en `frase-salida.txt` | 20 % |

## Pista de cara al futuro

Cada método trabaja sobre el resultado del anterior. Si haces `upper` antes de `strip`, los espacios de los extremos también se quedan en el texto en mayúsculas.
