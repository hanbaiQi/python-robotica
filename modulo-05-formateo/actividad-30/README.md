# Actividad 30 — Tres sensores, tres líneas

- *Módulo*: 5 · Formateo de cadenas
- *Fecha límite de entrega*: domingo 22 de noviembre de 2026, 23:59
- *RA 5*: b) Se han aplicado formatos en la visualización de la información.

## Contexto

Cada sensor tiene nombre y distancia. Una línea por sensor, con la distancia a un decimal, se lee de un vistazo.

## Objetivo

Mostrar tres sensores con f-strings, cada uno en su línea y con un decimal.

## Lo que debes hacer

1. Crea `solucion/sensores.py`.
2. Declara estas distancias: `ultrasonidos = 40`, `infrarrojos = 12.5` y `luz = 7`.
3. Muestra tres líneas, una por sensor. Cada línea es un f-string con el nombre del sensor y su distancia en el formato `{valor:.1f}`.
4. Ejecuta el programa y guarda la salida en `solucion/sensores-salida.txt`.

## Entregable

- `solucion/sensores.py`.
- `solucion/sensores-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Hay tres líneas, una por sensor | 30 % |
| Cada línea es un f-string con el nombre y la distancia | 30 % |
| Cada distancia se muestra con un decimal | 20 % |
| La salida está guardada en `sensores-salida.txt` | 20 % |

## Pista de cara al futuro

El nombre que escribes fuera de las llaves sale tal cual. El valor que está dentro se formatea.
