# Esto es un comentario de linea

# print () es una funcion que tiene salida por la consola
# "Hola mundo" es un lietral
print("Hola mundo")

"""
Esto es un comentario
de varias lineas
"""

"""
Trabajando con variables
- Nombre (Iniciar con una letra o un guion bajo _)
- Valor
- Tipo de dato
"""
nombre = "Romy"
print(nombre)

print ("Tipo de dato de la variable nombre: ", type(nombre))

"""
print("Romy", "Vergara") # Varios argumentos
print("Romy" + " " + "Vergara") # Concatenacion
"""

# Metodos en variables
print(nombre.upper())

# Asignar tipo de dato
apellido:str="Vergara"
print((apellido), type(apellido))

# Cambiar tipo de dato de la misma variable
# Originalmente tenemos la variable apellido declarada como str
# Cambiar su valor y tipos de datos no es un probelma para Python
# El error que recibimos es de vscode# 
apellido=10
print((apellido), type(apellido))

# Posicion de memoria de una variable
# id() funcion que permite conocer la posicion de memoria
# donde esta almacenada la varable
print(id(apellido))

# Tipo de dato numerico
edad= 25
print("Edad:", edad, type(edad))

# Operadores matematicos
# +  Suma
# -  Resta
# *  Multiplicacion
# /  Division
# // Division entera (retorna int)
# %  Modulo/Resto de la division
# ** Potencia

# Comportamiento de numers enteros
numero_entero_1 = 10
numero_entero_2 = 20
print("Sumando numeros enteros: ", numero_entero_1 + numero_entero_2) 
print("Resta numeros enteros: ", numero_entero_1 - numero_entero_2)
print("Multiplicacion numeros enteros: ", numero_entero_1 * numero_entero_2)

# La division retorna un float
print("Division: ", 7/2, type(7/2))
print("Division: ", 2/2, type(2/2))

# La division retorna un int
print("Division (int): ", 7//2, type(7//2))
print("Division (int): ", 2//2, type(2//2))

# Modulo o resto de la division
print("Division (modulo): ", 7%2, type(7%2))
print("Division (modulo): ", 2%2, type(2%2))

# Caso de uso
# Numeros de paginas para paginacion
elementos = 33
por_pagina = 10
print("Tenemos", elementos // por_pagina, "paginas")

# Saber si un numero es par
if (10 % 2) == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# Comportamiento de cadenas de texto
ciudad = "La Serena"
av = "10"

print(ciudad + av) # Usamos el operador + para concatenar variables str

# Conversion de tipo de datos
av_numero = 10

print(ciudad + str(av_numero)) # str() hace una coversion de int a str

# Otro ejemplo
n1 = "10"
n2 = "20"

print("Conctenando n1+n2", n1 + n2)

# Trabajamos con input()
print()
print("Sumar dos numeros")
print("-----------------")
primer_numero = input("Ingrese el primer numero:")
segundo_numero = input("Ingrese el segundo numero")

# Aqui concatena porque input devuelve un str
print("La suma de los dos numeros es:", primer_numero + segundo_numero)

# Conversion de tipo d dato
print("La suma de los dos numeros es:", int(primer_numero) + int(segundo_numero))

# Usando f-string
suma_str = f"La suma de {primer_numero} con {segundo_numero} es: {int(primer_numero) + int(segundo_numero)}"
suma_otro = (
    "La suma de"
    + primer_numero
    + " con "
    + segundo_numero
    + "  es: "
    + str(int(primer_numero) + int(segundo_numero))
)
print(suma_str)
print(suma_otro)

