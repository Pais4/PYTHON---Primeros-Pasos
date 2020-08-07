# Modulo de fechas

# Este modulo ya viene pre-instalado - Tiempo
import datetime

# Modulo de matematicas
import math

# Modulo random
import random

fechaCompleta = datetime.datetime.now()

print(fechaCompleta.day)
print(fechaCompleta.year)

print('Raiz cuadrada de 10', math.sqrt(10))
print('Numero PI:', float(math.pi))

print('Numero aleatorio entre 0 y 100:', random.randint(1, 100))