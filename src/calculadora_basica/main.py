def sumar(x, y):
    print(f"El resultado de la suma es: {x + y}")

def restar(x, y):
    print(f"El resultado de la resta es: {x - y}")

def multiplicar(x, y):
    print(f"El resultado de la multiplicación es: {x * y}")

def dividir(x, y):
    print(f"El resultado de la división es: {x / y}") 

def tomar_datos():
    x = int(input("Ingrese el primer número: "))
    y = int(input("Ingrese el segundo número: "))
    return x, y 

print("Calculadora básica")
print("------------------")
print("Qué operación desea realizar?")
print("1. Sumar dos números")
print("2. Restar dos números")
print("3. Multiplicar dos números")
print("4. Dividir dos números")
print("5. Salir")

opcion = input(">")


# Realizamos esta refactorizacion para tener un solo punto
# de ingreso de datos del usuario
# mas adelante vamos a cambiar la opcion tomar_datos()
# entonces debemos asegurar tener un solo punto de ingreso de datos del usuario

if opcion in ("1", "2", "3", "4"):
    x, y = tomar_datos()
    if opcion == "1":
        sumar(x, y)
    elif opcion == "2":
        restar(x, y)
    elif opcion == "3":
        multiplicar(x, y)
    elif opcion == "4":
        dividir(x, y)
    elif opcion == "5":
        print("Saliendo de la calculadora...")
else:
    print("Opción no válida. Por favor, seleccione una opción válida.")


# Tipado de int y float

 

