# Actividad 43 — Solo if

- *Módulo*: 7 · Condiciones
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: a) Se ha escrito y probado código que haga uso de estructuras de selección.

## Contexto

`if` ejecuta un bloque solo cuando la condición es verdadera. La sangría dice qué líneas están dentro.

## Objetivo

Imprimir «atrás» solo cuando la distancia es menor de 10 cm.

## Lo que debes hacer

1. Crea `solucion/solo-if.py`.
2. Declara `distancia_corta = 5` y `distancia_larga = 40`.
3. Muestra `distancia_corta`. Después, con un `if`, muestra `"atrás"` solo si `distancia_corta < 10`.
4. Muestra `distancia_larga`. Después, con otro `if`, muestra `"atrás"` solo si `distancia_larga < 10`.
5. La orden va sangrada dentro de cada `if`.
6. Ejecuta el programa y guarda la salida en `solucion/solo-if-salida.txt`.

La distancia de 40 cm no cumple la condición, así que no imprime «atrás».

## Entregable

- `solucion/solo-if.py`.
- `solucion/solo-if-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Hay un `if` para cada distancia, con la comparación `< 10` | 40 % |
| «atrás» está sangrado dentro del `if` | 20 % |
| Solo la distancia de 5 cm imprime «atrás» | 20 % |
| La salida está guardada en `solo-if-salida.txt` | 20 % |

## Pista de cara al futuro

Lo que no está sangrado se ejecuta siempre. Lo que está dentro del `if` solo se ejecuta si la condición es verdadera.
