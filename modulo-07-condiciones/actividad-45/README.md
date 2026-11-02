# Actividad 45 — If, elif, else

- *Módulo*: 7 · Condiciones
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: a) Se ha escrito y probado código que haga uso de estructuras de selección.

## Contexto

`elif` prueba otra condición cuando las anteriores no se han cumplido. El primero que se cumple gana, y el resto no se mira.

## Objetivo

Elegir una orden de batería con `if`, `elif` y `else`.

## Lo que debes hacer

1. Crea `solucion/elif.py`.
2. Declara `bateria = 35`.
3. Escribe un solo bloque:
   - si `bateria` es menor de 20, muestra `"parar"`;
   - si no, y es menor de 50, muestra `"lento"`;
   - si no, muestra `"adelante"`.
4. Usa `if`, `elif` y `else`. Cada orden va sangrada en su rama.
5. Ejecuta el programa y guarda la salida en `solucion/elif-salida.txt`.

## Entregable

- `solucion/elif.py`.
- `solucion/elif-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| El bloque tiene `if`, `elif` y `else` | 40 % |
| Con 35 se muestra «lento» | 40 % |
| La salida está guardada en `elif-salida.txt` | 20 % |

## Pista de cara al futuro

35 no es menor de 20, así que el `if` se salta. Sí es menor de 50, así que entra en el `elif` y el `else` no se ejecuta.
