lectura = ' el sensor mide distancia '
limpia = lectura.strip()
mayusculas = limpia.upper()
print(mayusculas)
print(len(mayusculas))
palabras = mayusculas.split()
print('-'.join(palabras))