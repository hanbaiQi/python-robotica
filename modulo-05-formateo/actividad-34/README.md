# Actividad 34 — La tabla de sensores

- *Módulo*: 5 · Formateo de cadenas
- *Fecha límite de entrega*: domingo 22 de noviembre de 2026, 23:59
- *RA 5*: b) Se han aplicado formatos en la visualización de la información.

## Contexto

Tres sensores, tres líneas. En cada línea van el nombre, la distancia con un decimal y la barra de `#`.

## Objetivo

Montar la tabla de la diapositiva con f-strings y la barra de cada 5 cm.

## Lo que debes hacer

1. Crea `solucion/tabla.py`.
2. Usa estas distancias, en centímetros: ultrasonidos 40, infrarrojos 12 y luz 7.
3. Para cada sensor, calcula su barra con `"#" * (distancia // 5)`.
4. Muestra una línea por sensor con un f-string. En la línea están el nombre, la distancia con `{distancia:.1f}` y la barra.
5. Ejecuta el programa y guarda la salida en `solucion/tabla-salida.txt`.

## Entregable

- `solucion/tabla.py`.
- `solucion/tabla-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Hay una línea por sensor, con su nombre | 25 % |
| Cada distancia se muestra con un decimal | 25 % |
| Cada línea incluye su barra de `#`, un carácter cada 5 cm | 30 % |
| La salida está guardada en `tabla-salida.txt` | 20 % |

## Pista de cara al futuro

La barra de 40 cm tiene ocho `#`. La de 12 tiene dos. La de 7 tiene uno, porque 7 entre 5 cabe una vez.
