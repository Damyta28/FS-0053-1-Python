# Mostrar menu por consola
def mostrar_menu(x: str = "Cualquier cosa") -> None:
    """
    Muestra un menu de opciones por consola
    """
    print(x)
    print("Seleccione una opción:")
    print("1. De acuerdo")
    print("2. En desacuerdo")
    print("3. No me interesa")

# Python simepre regresa un valor desde una funcion
# En el caso de no ser especificado, Python retorna
# None
# return 1


# Documentar funcion

preguntas = [
    "Enunciado pregunta 1",
    "Enunciado pregunta 2",
    "Enunciado pregunta 3"
    ]

respuestas = []



print(preguntas[0])
prueba = mostrar_menu()
respuestas.append(input('> '))

print(preguntas[1])
prueba = mostrar_menu("Hola x")
respuestas.append(input('> '))

print(preguntas[2])
prueba = mostrar_menu()
respuestas.append(input('> '))

print(f"La respuesta a la pregunta 1 es: {respuestas[0]}")
print(f"La respuesta a la pregunta 2 es: {respuestas[1]}")
print(f"La respuesta a la pregunta 3 es: {respuestas[2]}")
print(f"El valor devuelto por la funcion es: {prueba}")