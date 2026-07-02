# Mostrar menu por consola
def mostrar_menu(x: str = "Cualquier cosa") -> None:
    """
    Muestra un menu de opciones por consola\n
    x = Pregunta a ser realizada
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

for pregunta in preguntas:  
    prueba = mostrar_menu()
    respuestas.append(input('> '))

print()
print("Las respuestas son:")
print("-------------------")
for i, respuesta in enumerate(respuestas):
    print(f"Pregunta {i + 1}: {respuesta}")

print("Muchas gracias por participar en la encuesta")