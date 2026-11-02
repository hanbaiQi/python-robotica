# Actividad 49 — Anidar

- *Módulo*: 7 · Condiciones
- *Fecha límite de entrega*: domingo 29 de noviembre de 2026, 23:59
- *RA 3*: a) Se ha escrito y probado código que haga uso de estructuras de selección.

## Contexto

Un `if` puede ir dentro de otro. Primero se mira si el robot está encendido. Solo si lo está, la distancia decide la orden. Si está apagado, la orden es «apagado».

## Objetivo

Anidar un `if` de distancia dentro de un `if` de encendido, y probar los dos estados.

## Lo que debes hacer

1. Crea `solucion/anidar.py`.
2. Para un robot encendido y cerca del obstáculo, declara `encendido = True` y `distancia = 5`.
3. Escribe este esquema, con la sangría de cada nivel:
   - si `encendido` es verdadero, mira la distancia: si es menor de 10, muestra `"atrás"`; si no, muestra `"adelante"`;
   - si `encendido` es falso, muestra `"apagado"`.
4. Repite el mismo esquema con `otro_encendido = False` y `otra_distancia = 5`.
5. Ejecuta el programa y guarda la salida en `solucion/anidar-salida.txt`.

## Entregable

- `solucion/anidar.py`.
- `solucion/anidar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| El `if` de la distancia está dentro del `if` de encendido | 40 % |
| Con el robot encendido y a 5 cm se muestra «atrás» | 20 % |
| Con el robot apagado se muestra «apagado» | 20 % |
| La salida está guardada en `anidar-salida.txt` | 20 % |

## Pista de cara al futuro

La distancia solo se mira si el `if` de fuera se ha cumplido. El `else` de fuera corresponde al robot apagado, no a la distancia.
