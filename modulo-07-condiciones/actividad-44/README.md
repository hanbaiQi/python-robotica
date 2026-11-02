# Actividad 44 — If y else

- *Módulo*: 7 · Condiciones
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: a) Se ha escrito y probado código que haga uso de estructuras de selección.

## Contexto

`else` es el camino de cuando el `if` no se cumple. Uno de los dos bloques se ejecuta siempre.

## Objetivo

Decidir «parar» o «seguir» según la batería, y probar los dos casos.

## Lo que debes hacer

1. Crea `solucion/if-else.py`.
2. Declara `bateria_baja = 10` y `bateria_alta = 80`.
3. Para `bateria_baja`, escribe un `if` / `else`: si es menor de 20, muestra `"parar"`; si no, muestra `"seguir"`.
4. Repite el mismo `if` / `else` para `bateria_alta`.
5. Los dos `print` van sangrados, cada uno en su bloque.
6. Ejecuta el programa y guarda la salida en `solucion/if-else-salida.txt`.

## Entregable

- `solucion/if-else.py`.
- `solucion/if-else-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Cada batería tiene su `if` y su `else` | 30 % |
| Menos de 20 muestra «parar» y el otro caso muestra «seguir» | 30 % |
| La sangría separa los dos bloques | 20 % |
| La salida está guardada en `if-else-salida.txt` | 20 % |

## Pista de cara al futuro

Con 10 tiene que salir «parar». Con 80 tiene que salir «seguir». Son dos bloques iguales, con una variable distinta cada uno.
