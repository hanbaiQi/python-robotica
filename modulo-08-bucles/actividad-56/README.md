# Actividad 56 — La batería baja con while

- *Módulo*: 8 · Bucles
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: b) Se han utilizado estructuras de repetición.

## Contexto

El robot sale con la batería a 100. Cada tramo de marcha gasta 20. Sigue mientras quede carga.

## Objetivo

Restar 20 a la batería con un `while` e imprimir lo que queda en cada vuelta.

## Lo que debes hacer

1. Crea `solucion/bateria.py`.
2. Empieza con `bateria = 100`.
3. Escribe `while bateria > 0:`.
4. Dentro del `while`, resta 20 a `bateria` e imprime lo que queda.
5. Ejecuta el programa y guarda la salida en `solucion/bateria-salida.txt`.

La salida son cinco líneas: 80, 60, 40, 20 y 0. Cuando `bateria` llega a 0, la condición `bateria > 0` ya no se cumple y el bucle termina.

## Entregable

- `solucion/bateria.py`.
- `solucion/bateria-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| `bateria` empieza en 100 y la condición del `while` es `bateria > 0` | 25 % |
| En cada vuelta se restan 20 | 25 % |
| Se imprimen 80, 60, 40, 20 y 0 | 35 % |
| La salida está guardada en `bateria-salida.txt` | 15 % |

## Pista de cara al futuro

Cada vuelta del `while` gasta 20 de batería hasta que el robot se queda a cero.
