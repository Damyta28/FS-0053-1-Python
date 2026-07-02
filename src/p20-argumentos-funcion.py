def extremo_multiplicado(lista, factor):
    print(type(lista))
    print(type(factor))
    print(variable_global)
    
    # minimo = min(lista)
    # maximo = max(lista)
    # return minimo * factor, maximo * factor

variable_global = 100

# Llamada correcta
# Argumentos por posicion

print(
    extremo_multiplicado([1, 2, 3, 4], 4))

# Llamada incorrecta
# Argumentos por posicion

print(
    extremo_multiplicado(4, [1, 2, 3, 4]))

# Llamada incorrecta
# Argumentos por nombre

print(
    extremo_multiplicado(factor=4, lista=[1, 2, 3, 4])) 