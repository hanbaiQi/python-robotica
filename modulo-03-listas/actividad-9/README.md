# Actividad 9 — Los sensores, en una lista

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 1 de noviembre de 2026, 23:59
- *RA 1*: d) Se han identificado los distintos tipos de variables y la utilidad específica de cada uno.

## Contexto

Hasta ahora cada dato del robot vivía en su propia variable. Cuando hay varios sensores, conviene guardarlos juntos, en orden, en una sola lista.

## Objetivo

Crear una lista de textos y comprobar que su tipo es `list`.

## Lo que debes hacer

1. Crea `solucion/sensores.py`.
2. Declara una lista llamada `sensores` con estos cuatro nombres, en este orden: `"ultrasonidos"`, `"infrarrojos"`, `"luz"`, `"temperatura"`.
3. Muestra la lista completa en una línea.
4. Muestra el tipo de `sensores` con `type()`. Tiene que verse que es una lista.
5. Ejecuta el programa y guarda la salida en `solucion/sensores-salida.txt`.

## Entregable

- `solucion/sensores.py`.
- `solucion/sensores-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| La lista tiene los cuatro sensores en el orden pedido | 40 % |
| Se muestra la lista completa | 20 % |
| `type()` muestra que el valor es una lista | 20 % |
| La salida está guardada en `sensores-salida.txt` | 20 % |

## Pista de cara al futuro

Una lista es un solo nombre para muchos valores. El orden en el que los escribes es el orden en el que se quedan.
