# Actividad 13 — Se estropea un sensor

- *Módulo*: 3 · Listas
- *Fecha límite de entrega*: domingo 8 de noviembre de 2026, 23:59
- *RA 1*: e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

Cuando un sensor deja de funcionar, hay que quitarlo de la lista. `remove(valor)` busca ese valor y borra la primera vez que aparece. Busca el dato, no la posición.

## Objetivo

Quitar un valor concreto de una lista y comprobar el resultado.

## Lo que debes hacer

1. Crea `solucion/quitar.py`.
2. Declara `sensores = ["ultrasonidos", "infrarrojos", "luz", "temperatura"]`.
3. Muestra la lista.
4. Quita `"luz"` con `remove("luz")`. El valor tiene que estar en la lista.
5. Vuelve a mostrar la lista. `"luz"` ya no debe aparecer, y el resto conserva su orden.
6. Ejecuta el programa y guarda la salida en `solucion/quitar-salida.txt`.

## Entregable

- `solucion/quitar.py`.
- `solucion/quitar-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Se muestra la lista antes de quitar | 25 % |
| `"luz"` se elimina con `remove()`, buscando el valor | 35 % |
| Se muestra la lista después, sin ese sensor y con el resto en orden | 20 % |
| La salida está guardada en `quitar-salida.txt` | 20 % |

## Pista de cara al futuro

`remove()` no pide un índice. Si el mismo valor estuviera dos veces, solo desaparecería la primera. Aquí cada sensor aparece una sola vez.
