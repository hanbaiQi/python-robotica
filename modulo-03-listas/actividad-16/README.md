# Actividad 16 — La misión de los sensores

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 8 de noviembre de 2026, 23:59
- *RA 1*: d) Se han identificado los distintos tipos de variables y la utilidad específica de cada uno. e) Se ha modificado el código de un programa para crear y utilizar variables.
- *RA 2*: b) Se han escrito programas simples.

## Contexto

El robot lleva los nombres de los sensores en una lista y las distancias, en centímetros, en otra. Las dos van alineadas: el nombre de la posición 0 corresponde a la distancia de la posición 0. En esta actividad juntas lo que ya sabes hacer con una lista.

`sorted()` solo mira la lista que le pasas. Ordenar las distancias deja los nombres donde estaban.

## Objetivo

Añadir un sensor, quitar otro y leer la distancia más cercana y la más lejana, manteniendo las dos listas del mismo tamaño.

## Lo que debes hacer

1. Crea `solucion/mision.py`.
2. Declara estas dos listas, ya alineadas:
   - `sensores = ["ultrasonidos", "infrarrojos", "luz"]`
   - `distancias = [40, 12, 80]`
3. Añade el sensor de presencia al final de las dos: `"presencia"` en `sensores` y `5` en `distancias`. Usa `append()` en cada una.
4. Quita el sensor de luz de las dos: `remove("luz")` en `sensores` y `remove(80)` en `distancias`.
5. Muestra `len(sensores)` y `len(distancias)`. Tienen que coincidir.
6. Guarda `sorted(distancias)` en `ordenadas`. Muestra el más cercano, `ordenadas[0]`, y el más lejano, `ordenadas[-1]`.
7. Muestra los dos primeros nombres que mirará el robot con `sensores[0:2]`.
8. Ejecuta el programa y guarda la salida en `solucion/mision-salida.txt`.

Ordenar `distancias` no cambia el orden de `sensores`. Cada cambio y cada impresión va en su propia línea.

## Entregable

- `solucion/mision.py`.
- `solucion/mision-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Presencia se añade, con su distancia, al final de las dos listas | 25 % |
| Luz y su distancia se quitan con `remove()` y las dos longitudes coinciden | 25 % |
| El más cercano y el más lejano salen de `sorted()` | 25 % |
| Se muestra el corte de los dos primeros sensores | 15 % |
| La salida está guardada en `mision-salida.txt` | 10 % |

## Pista de cara al futuro

Dos listas alineadas siguen alineadas si cada alta y cada baja la haces en las dos. Más adelante verás formas de guardar el nombre y la distancia juntos; por ahora, ese cuidado es tuyo.
