from io import open
import pathlib

# El path nos ayuda a saber la ruta actual
# print(pathlib.Path().absolute())

# Abrir archivos
ruta = str(pathlib.Path().absolute()) + '/fichero_texto.txt'
archivo = open(ruta, 'a+')

# Escribir
archivo.write('Hola Mundo')

# Cerrar el archivo
archivo.close()

# Leer archivo
lecturaArchivo = open(ruta, 'r')
print(lecturaArchivo.read())