print("Estructura de datos en Python")
print("-----------------------------\n")

# Listas
print("Listas (list)")
print("-------------")

# Indice:      0       1         2            3
# Negativo    -4      -3        -2           -1
fullstack = ["HTML", "CSS", "JavaScript", "Python"]
print(fullstack)

print(f"El tipo de dato es: {type(fullstack)}")

# Acceder a un elemento de una lista
print(fullstack[2])  # JavaScript
print(fullstack[-1])  # Ultimo elemento de la lista
# print(fullstack[10])  List index out of range

# Agregar elemento a la lista
fullstack.append("Base de datos")

# Cambiar valor
fullstack[3] = "Python 3.13"

print(fullstack)

# Una lista de listas 
simulando_matriz = [
    [1,2,3],
    [4,5,6],
]
print(simulando_matriz)
print()

# --------------------------------------------------------
# Tuplas
titulo = "Tuplas (tuples) esto es un ejemplo dinamico de repetir caracteres"
print(titulo)
print("-" * len(titulo))

curso = ("Bootcamp", "Fullstack", "Python", "2026")
print(curso)

print(f"El tipo de dato es: {type(curso)}")

# Cambiar valores en una tupla
# Las tuplas no pueden cambiar de valor porque son inmutables
# curso.append() no existe
# curso[1] = fullstack  # "tuple" object does not support item assignment

# Curiosidad de ciencias de la computacion
# Una cadena de texto se comporta como una lista
nombre = "Romina"
print(type(nombre), nombre[3])
print()

# --------------------------------------------------------
# Set
titulo = "Set (set)"
print(titulo)
print("-" * len(titulo))

# Set no permite valores repetidos (no arroja error, pero ignora los duplicados)
lenguajes = { "Python", "JavaScript", "PHP", "C#", "Elixir", "Java", "Python" }
print(lenguajes)

print(f"El tipo de dato es: {type(lenguajes)}")

lista_duplicada = [1, 2, 3, 4, 1, 6, 1]
print(set(lista_duplicada))


# --------------------------------------------------------
# Diccionario