# Dunder methods
lista = {1, 2, 3, 4, 5, 6, }

# print( lista.__dir__())

# Tamaño del objeto
# print( len(lista))
# print(lista.__len__)

# help( lista.pop)
print("Metodo apped")
print("------------")

colores = ['verde', 'rojo', 'rosa', 'azul']
colores.append( 'celeste' )

print( colores )

# Inicializzcion de variable
colores = []

# Agregamos valores a la lista
# Normalmente esto queda
# dentro de un for
colores.append( 'rojo' )
colores.append( 'rosa' )
colores.append( 'azul' )
colores.append( 'celeste' )

print( colores )
print()

print( "Metodo insert" )
print( "--------------")

#                0    1    2    3    4
lista_puntos = [".", ".", ".", ".", "."]
print(lista_puntos)

#  0    1    2    3    4
# ".", ".", ".", ".", "."

lista_puntos.insert(2, "-")
print( lista_puntos )

#  0    1    2    3    4    5
# ".", ".", "-", ".", ".", "."

lista_puntos.insert(-1, "*")
print( lista_puntos )
print()


print( "Metodo pop" )
print( "----------" )

print( colores )

color_eliminado = colores.pop(2)

print( "Lista", colores)
print(f"Color eliminado: {color_eliminado}")
print()

print( "Metodo remove" )
print( "-------------" )

# Recibe el valor a eliminar
# Elimina la primera ocurrencia
# Retorna none
# Si el valor no existe se genera un error

numeros = [ 100, 400, 50, 200, 50, 300 ]

numero_eleminado = numeros.remove(50)

print( "Lista", numeros)
print()

print( "Metodo reverse() y sort" )
print( "------------" )
# [WARNING] Modifica la lista

# Invierte el orden actual
numeros.reverse()
print( "Lista con orden cambiado", numeros)

# Ordena una lista de forna ascendente
numeros.sort()
print("Lista ordenada[asc]", numeros)

# Ordena una lista descendente
numeros.sort(reverse = True)
print( "LIsta ordenada [desc]", numeros)
print()

print( "Funcion sorted" )
print( "--------------" )
# Crea una nueva lista ordenada
# Mantiene la lista original sin cambios

numeros_aux = [ 100, 400, 200, 50, 300 ]

lista_ordenada = sorted( numeros_aux, reverse = True)

print( "Lista original", numeros_aux)
print( "Lista ordenada", lista_ordenada)



