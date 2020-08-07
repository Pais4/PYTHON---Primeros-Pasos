#Creacion de variables
texto = 'Master en Python'
entero = 23
decimal = 2.344

#Asignar valores a multiples variables
x, y, z = 'Orange', 'Banana', 'Apple'

print( x )
print( y )
print( z )

# Con el uso de la f podemos incluir las variables 
# directamente dentro de la cadena
print(f'{x} {y} and an {z}')

# Otra forma de concatenar es usando le funcion format
print('Hi, i have an {}, a {} and the lastone is an {}'.format(x, y, z))