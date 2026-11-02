# Actividad 33 — La barra

- *Módulo*: 5 · Formateo de cadenas
- *Fecha límite de entrega*: domingo 22 de noviembre de 2026, 23:59
- *RA 5*: b) Se han aplicado formatos en la visualización de la información.

## Contexto

Una barra de `#` cuenta la distancia a ojo: un `#` por cada 5 cm. `"#" * n` repite el carácter n veces.

## Objetivo

Construir una barra proporcional a una distancia.

## Lo que debes hacer

1. Crea `solucion/barra.py`.
2. Declara `distancia = 20`.
3. Guarda en `barra` el resultado de `"#" * (distancia // 5)`.
4. Muestra `barra`.
5. Ejecuta el programa y guarda la salida en `solucion/barra-salida.txt`.

## Entregable

- `solucion/barra.py`.
- `solucion/barra-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| La barra se calcula con `"#" * (distancia // 5)` | 50 % |
| Se muestra la barra | 30 % |
| La salida está guardada en `barra-salida.txt` | 20 % |

## Pista de cara al futuro

`//` dice cuántos grupos de 5 cm caben. Multiplicar el texto `"#"` por ese número repite el carácter.
