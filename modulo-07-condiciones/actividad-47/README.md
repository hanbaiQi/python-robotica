# Actividad 47 — Or

- *Módulo*: 7 · Condiciones
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: a) Se ha escrito y probado código que haga uso de estructuras de selección.

## Contexto

Hay que parar si la batería está por debajo de 20 o si hay una pared. Con que una de las dos sea cierta, basta. `or` lo expresa.

## Objetivo

Probar las tres combinaciones de batería y pared.

## Lo que debes hacer

1. Crea `solucion/or.py`.
2. Escribe tres bloques `if` / `else`, uno por caso. La condición es `bateria < 20 or hay_pared`. Si se cumple, muestra `"parar"`. Si no, muestra `"seguir"`.
3. Los tres casos son:
   - `bateria = 10` y `hay_pared = False`;
   - `bateria = 80` y `hay_pared = True`;
   - `bateria = 80` y `hay_pared = False`.
4. Usa un nombre de variable distinto en cada caso, para no pisar el anterior.
5. Ejecuta el programa y guarda la salida en `solucion/or-salida.txt`.

## Entregable

- `solucion/or.py`.
- `solucion/or-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Cada caso usa `or` en el `if` | 30 % |
| Los dos primeros casos muestran «parar» | 25 % |
| El tercer caso muestra «seguir» | 25 % |
| La salida está guardada en `or-salida.txt` | 20 % |

## Pista de cara al futuro

`or` entra en el `if` si la batería es baja, si hay pared, o si pasan las dos cosas. Solo se va al `else` cuando las dos son falsas.
