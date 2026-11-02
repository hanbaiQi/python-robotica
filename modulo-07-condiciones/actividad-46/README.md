# Actividad 46 — And

- *Módulo*: 7 · Condiciones
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: a) Se ha escrito y probado código que haga uso de estructuras de selección.

## Contexto

El robot acelera a tope solo si se cumplen las dos cosas: batería por encima de 80 y velocidad por encima de 60. `and` une las dos comparaciones dentro del `if`.

## Objetivo

Probar un `if` con `and` en un caso que acelera y en otro que no.

## Lo que debes hacer

1. Crea `solucion/and.py`.
2. Declara `bateria = 90` y `velocidad = 70`.
3. Si `bateria > 80 and velocidad > 60`, muestra `"acelerar"`. Si no, muestra `"esperar"`.
4. Declara `velocidad_baja = 40`. Repite el mismo `if` / `else` con `bateria` y `velocidad_baja`.
5. Ejecuta el programa y guarda la salida en `solucion/and-salida.txt`.

## Entregable

- `solucion/and.py`.
- `solucion/and-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| La condición del `if` usa `and` con las dos comparaciones | 40 % |
| El caso 90 y 70 muestra «acelerar» | 20 % |
| El caso 90 y 40 muestra «esperar» | 20 % |
| La salida está guardada en `and-salida.txt` | 20 % |

## Pista de cara al futuro

Con `and`, basta que una de las dos comparaciones sea falsa para que no se entre en el `if`.
