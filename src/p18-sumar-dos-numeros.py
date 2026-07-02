# Código original: src/sumar-dos-numeros.py
# Hacemos que trabaje con funciones
# Refactorizacion
# - Validacion del valor ingresado

# La funcion valida si un valor es un número de tipo entero (int)
# Retorno tipo booleano
# - Entero = True
def es_numero(valor):
    return valor.isdigit()

# Muetra un mesaje de rror en consola
# texto = Posicion de ingreso del valor
# valor_error = Valor ingresado
def msj_error(texto, valor_error):
    print("Error!!!")
    print("Los valores ingresados deben ser numeros enteros")
    print(f"{texto} numero es: {valor_error}")

def sumar_dos_numeros(n1, n2):
    suma = int(n1) + int(n2)
    return suma

# -------------------
n1 = input ("Ingrese el primer número: ")
n2 = input ("Ingrese el segundo número: ")

if not es_numero(n1):
    msj_error("Primero", n1)
    sys.exit() 

if not es_numero(n2):
    msj_error("Segundo", n2)
    sys.exit()

    n1 = int(n1)
    n2 = int(n2)
    
    suma = sumar_dos_numeros(n1, n2)
    
    print(f"La suma de los números es: {suma}")
