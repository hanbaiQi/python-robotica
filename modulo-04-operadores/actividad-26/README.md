# Actividad 26 — No, y el robot

- *Módulo*: 4 · Operadores básicos
- *Fecha límite de entrega*: domingo 15 de noviembre de 2026, 23:59
- *RA 1*: g) Se han clasificado, reconocido y utilizado en expresiones los operadores del lenguaje.

## Contexto

`not` invierte un verdadero o un falso. Con la batería justa, el robot no puede acelerar a tope y sí debería parar. Además hace tres cuentas: tramos enteros de autonomía, lo que sobra y una potencia.

## Objetivo

Usar `not`, `//`, `%` y `**` en el mismo programa.

## Lo que debes hacer

1. Crea `solucion/acelerar.py`.
2. Declara `bateria = 15` y `velocidad = 70`.
3. Muestra el resultado de `bateria > 80 and velocidad > 60`.
4. Muestra el resultado de `not (bateria > 20)`. Esa expresión es la de «debería parar».
5. Declara `minutos = 100`, `gasto = 30` y `voltaje = 3`. Muestra, cada uno en su línea:
   - `minutos // gasto`
   - `minutos % gasto`
   - `voltaje ** 2`
6. Ejecuta el programa y guarda la salida en `solucion/acelerar-salida.txt`.

## Entregable

- `solucion/acelerar.py`.
- `solucion/acelerar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Se muestra la expresión con `and` y la expresión con `not` | 40 % |
| Se muestran la división entera, el resto y la potencia | 40 % |
| La salida está guardada en `acelerar-salida.txt` | 20 % |

## Pista de cara al futuro

`not` cambia el sentido de la comparación que tiene al lado. Los paréntesis dejan claro qué es lo que se invierte.
