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

# -------------------
n1 = input ("Ingrese el primer número: ")
n2 = input ("Ingrese el segundo número: ")

if not es_numero(n1):
    msj_error("Primero", n1)

if not es_numero(n2):
    msj_error("Segundo", n2)

if es_numero(n1) and es_numero(n2):
    n1 = int(n1)
    n2 = int(n2)
    
    suma = int(n1) + int(n2)
    
    print(f"La suma de {n1} y {n2} es: {suma}")
else:
    print("Por favor, ingrese números válidos.")