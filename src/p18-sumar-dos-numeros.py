# ódigo original: src/sumar-dos-numeros.py

n1 = input ("Ingrese el primer número: ")
n2 = input ("Ingrese el segundo número: ")

if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    
    suma = int(n1) + int(n2)
    
    print(f"La suma de {n1} y {n2} es: {suma}")
else:
    print("Por favor, ingrese números válidos.")