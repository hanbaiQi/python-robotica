# Actividad 25 — Y, o

- *Módulo*: 4 · Operadores básicos
- *Fecha límite de entrega*: domingo 15 de noviembre de 2026, 23:59
- *RA 1*: g) Se han clasificado, reconocido y utilizado en expresiones los operadores del lenguaje.

## Contexto

`and` solo es verdadero si las dos cosas lo son. `or` es verdadero si al menos una lo es. El robot puede acelerar a tope solo con batería alta y velocidad alta. Debe vigilar si la batería está baja o hay un obstáculo.

## Objetivo

Combinar comparaciones con `and` y con `or`.

## Lo que debes hacer

1. Crea `solucion/logicos.py`.
2. Declara `bateria = 90`, `velocidad = 70` y `hay_pared = False`.
3. Muestra el resultado de `bateria > 80 and velocidad > 60`.
4. Declara `bateria_baja = 15`. Muestra el resultado de `bateria < 20 or hay_pared` y el de `bateria_baja < 20 or hay_pared`.
5. Cada resultado va en su línea.
6. Ejecuta el programa y guarda la salida en `solucion/logicos-salida.txt`.

## Entregable

- `solucion/logicos.py`.
- `solucion/logicos-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| La aceleración a tope se expresa con `and` | 30 % |
| La batería baja o el obstáculo se expresan con `or` | 30 % |
| Se muestran los tres resultados | 20 % |
| La salida está guardada en `logicos-salida.txt` | 20 % |

## Pista de cara al futuro

`and` y `or` no eligen un camino. Devuelven `True` o `False`, igual que una comparación.
