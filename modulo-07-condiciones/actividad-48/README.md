# Actividad 48 — Not

- *Módulo*: 7 · Condiciones
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: a) Se ha escrito y probado código que haga uso de estructuras de selección.

## Contexto

`not` invierte la condición. `if not encendido` entra cuando el robot está apagado.

## Objetivo

Usar `not` dentro de un `if` y probar el robot encendido y apagado.

## Lo que debes hacer

1. Crea `solucion/not.py`.
2. Declara `encendido = False`.
3. Si `not encendido`, muestra `"apagado"`. Si no, muestra `"en marcha"`.
4. Declara `otro = True`. Repite el mismo `if` / `else` con `otro`.
5. Ejecuta el programa y guarda la salida en `solucion/not-salida.txt`.

## Entregable

- `solucion/not.py`.
- `solucion/not-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| La condición es `not` sobre el estado de encendido | 40 % |
| Con `False` se muestra «apagado» | 20 % |
| Con `True` se muestra «en marcha» | 20 % |
| La salida está guardada en `not-salida.txt` | 20 % |

## Pista de cara al futuro

`not False` es verdadero, así que se entra en el `if`. `not True` es falso, así que se va al `else`.
