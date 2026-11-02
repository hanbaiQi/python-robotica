# Actividad 50 — El sensor de distancia

- *Módulo*: 7 · Condiciones
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: a) Se ha escrito y probado código que haga uso de estructuras de selección.

## Contexto

El sensor manda la orden según lo cerca que esté el obstáculo: menos de 10 cm, atrás; menos de 30 cm, lento; en cualquier otro caso, adelante.

## Objetivo

Probar las tres ramas con tres distancias.

## Lo que debes hacer

1. Crea `solucion/sensor.py`.
2. Declara `cerca = 5`, `media = 20` y `lejos = 50`.
3. Para cada distancia, escribe un bloque `if` / `elif` / `else`:
   - menor de 10: muestra `"atrás"`;
   - menor de 30: muestra `"lento"`;
   - en otro caso: muestra `"adelante"`.
4. Antes de cada bloque, muestra la distancia, para saber a qué caso corresponde la orden.
5. Ejecuta el programa y guarda la salida en `solucion/sensor-salida.txt`.

## Entregable

- `solucion/sensor.py`.
- `solucion/sensor-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Cada distancia tiene su `if`, `elif` y `else` | 30 % |
| 5 cm muestra «atrás», 20 cm muestra «lento» y 50 cm muestra «adelante» | 50 % |
| La salida está guardada en `sensor-salida.txt` | 20 % |

## Pista de cara al futuro

20 no es menor de 10, así que no entra en «atrás». Sí es menor de 30, así que la orden es «lento» y el `else` no se ejecuta.
