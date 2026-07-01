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