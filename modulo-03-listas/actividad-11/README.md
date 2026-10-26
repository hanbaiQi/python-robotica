# Actividad 11 — Llega el de presencia

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 1 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

El robot no nace con todos los sensores puestos. `append()` añade un valor al final de la lista, que es el sitio donde llega lo nuevo.

## Objetivo

Añadir un elemento al final de una lista y comprobar que la lista y su longitud cambian.

## Lo que debes hacer

1. Crea `solucion/anadir.py`.
2. Declara `sensores = ["ultrasonidos", "infrarrojos", "luz"]`.
3. Muestra la lista y su longitud con `len()`.
4. Añade `"presencia"` al final con `append()`.
5. Vuelve a mostrar la lista y su longitud.
6. Ejecuta el programa y guarda la salida en `solucion/anadir-salida.txt`.

## Entregable

- `solucion/anadir.py`.
- `solucion/anadir-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Se muestra la lista y su longitud antes de añadir | 30 % |
| `"presencia"` se añade al final con `append()` | 30 % |
| Se muestra la lista y su longitud después de añadir | 20 % |
| La salida está guardada en `anadir-salida.txt` | 20 % |

## Pista de cara al futuro

`append()` modifica la lista que ya tienes. Hay que imprimirla otra vez para ver el cambio.
