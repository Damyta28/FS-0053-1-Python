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

if opcion == "1":
    x, y = tomar_datos()
    sumar(x, y)
elif opcion == "2":
    x, y = tomar_datos()
    restar(x, y)
elif opcion == "3":
    x, y = tomar_datos()
    multiplicar(x, y)
elif opcion == "4":
    x, y = tomar_datos()
    dividir(x, y)
elif opcion == "5":
    print("Saliendo de la calculadora...")
else:
    print("Opción no válida. Por favor, seleccione una opción válida.")

    
# Tipado de int y float

 

