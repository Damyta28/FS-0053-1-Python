# Esta sintaxis de int y float
# indica que puede recibir estos tipos de datos

def sumar(x: int | float, y: int | float):
    """
    fx que suma dos numeros
    """
    return x + y

# Al sacr el print() de la funcion y restornar 
# el resultado de la suma, ahora la funcion cumple con el principio de responsabilidad unica