# Actividad 23 — Comparar

- *Módulo*: 4 · Operadores básicos
- *Fecha límite de entrega*: domingo 15 de noviembre de 2026, 23:59
- *RA 1*: g) Se han clasificado, reconocido y utilizado en expresiones los operadores del lenguaje.

## Contexto

Una comparación no da un número nuevo. Da `True` o `False`: la batería es alta, la velocidad no llega, y así.

## Objetivo

Usar `<`, `>`, `<=` y `>=`, y ver que el resultado es verdadero o falso.

## Lo que debes hacer

1. Crea `solucion/comparar.py`.
2. Declara `bateria = 90` y `velocidad = 40`.
3. Muestra, cada una en su línea, estas cuatro comparaciones:
   - `bateria < 20`
   - `bateria > 80`
   - `velocidad <= 60`
   - `velocidad >= 60`
4. Ejecuta el programa y guarda la salida en `solucion/comparar-salida.txt`.

## Entregable

- `solucion/comparar.py`.
- `solucion/comparar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Están las cuatro comparaciones `<`, `>`, `<=` y `>=` | 40 % |
| Cada comparación se imprime y el resultado es `True` o `False` | 40 % |
| La salida está guardada en `comparar-salida.txt` | 20 % |

## Pista de cara al futuro

No hace falta un `if` para ver una comparación. `print` enseña el `True` o el `False` que devuelve.
