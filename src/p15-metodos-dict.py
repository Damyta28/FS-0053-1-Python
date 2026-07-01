print( "Agregar elementos a un diccionario (dict)" )
print( "-----------------------------------------" )

# Cuando haceos referencia a la clave de un dict
# que no existe, lo agrega
#
diccionario = { "llave 1": 5 }

print( diccionario )

diccionario[ "llave 2"] = 9

print( diccionario )

print()
print( "Cambiar calor de una clave de un diccionario (dict)" )
print( "---------------------------------------------------" )

diccionario["llave2"] = 18

print( diccionario )

print()
print( "Eliminar elemento" )
print( "-----------------" )

# Metodo pop

diccionario = {"celular": 140000, "notebook": 489990, "tablet": 120000, "cargador": 12400 }
print( "Diccionario original", diccionario)

# Metodod pop
# Elimina un elemnto de un dict usando la clave 'key'
# y devuelve el valor de dicho elemento
valor_eliminado = diccionario.pop("celular")
print (" - Eliminado 'celular'", diccionario)
print(f"Valor de 'celular' = {valor_eliminado}")


print()
print( "Actualizar diccionarios" )
print( "-----------------" )

diccionario_a = {"nomre": "Alejandra", "Apellido": "Lopez", "Edad": 33, "Altura": 1.55}
diccionario_b = {"mascota": "MITI", "ejercicio": "bicicleta"}

diccionario_a.update(diccionario_b)

print("Diccionario actualizado:", diccionario_a)

diccionario_c = {"edad": 40}
diccionario_a.update(diccionario_c)

print("Diccionario actualizado:", diccionario_a)

print()
print( "Metodo Keys()" )
print( "-------------" )

# Devuelve las claves de un diccionario  
# El objeto devuleto se puede:
# - Iterar
# - Validar contenido
# - Enlazado dinamicamente  

llaves = diccionario_a.keys()
print("Llaves del diccionario:", list(llaves))

# Se puede iterar
for aux in llaves:
    print(aux)  

# Validar si existe una llave
if "celular" not in llaves:
    print("La clave 'celular' no existe en el diccionario")
    print("Actualizando dict... Agregano nuevo elemento")
    diccionario['celular'] = 140000

print("NUevo diccionari", diccionario)
print("La variable llaves se actualiza dinamicamente")

print()
print( "Metodo value()" )
print( "--------------" )

# Comportamiento similar a Keys

valores = diccionario_a.values()
print("Valores del diccionario:", list(valores))

print()
print( "Metodo items()" )
print( "--------------" )

# Tiene un comportamiento similar a Keys y Values
# Regresa una lista de tuplas (clave, valor)

lista = diccionario.items()
print("Lista de tuplas (clave, valor):", list(lista))

for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

for i, (item) in enumerate(diccionario.items()):
    print(f"Elemento {i}: Clave: {item[0]}, Valor: {item[1]}")



