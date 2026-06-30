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

