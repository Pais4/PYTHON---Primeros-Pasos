# Funcion con retorno
def suma(num1, num2):
    return num1 * num2

# El metodo pass sigue con la ejecucion del programa
def funcion():
    pass

resultado = suma(3, 10)
print(resultado)

# Parametros opcionales 
def getEmpleado( nombre, dni = None ):
    print(f'El nombre es { nombre }')
    print(f'El dni es { dni }')
    
# Funciones lambda - Year -> Parametro : Retorno
getYear = lambda year: f'El año es { year }'
print(getYear(2020))

