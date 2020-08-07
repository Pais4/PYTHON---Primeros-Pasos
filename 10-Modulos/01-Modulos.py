# Los modulos son funcionalidades ya hechas para reutilizar
# https://docs.python.org/3/py-modindex.html

# Importamos el modulo completo
# import miModulo

# Si solo queremos importar una funcion del modulo
# from miModulo import suma

# Si queremos importar todas las funciones y no tener que llamarlas con el modulo adelante
from miModulo import *

# Asi seria teniendo todo el modulo importado
# print(miModulo.holaMundo('Mateo'))
# print(miModulo.suma(5, 10))

print(suma(40, 50))
