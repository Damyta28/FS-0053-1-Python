from sumar import sumar
from restar import restar

# Sumar envio dos numeros enteros
resp = sumar(10, 20)
if resp == 30:
    print("Test de suma: OK")
else:
    print("Test de suma: ERROR")    

# Sumar envio de un entero y una cadena
try:
    resp = sumar(10, "20")
    print("Test de suma con cadena: ERROR")
except TypeError:
    print("Test de suma con cadena: OK")

# Restar envio dos numeros enteros
resp = restar(10, 20)
if resp == -10:
    print("Test de resta: OK")
else:
    print("Test de resta: ERROR")

# Restar envio de un entero y una cadena
try:
    resp = restar(10, "20")
    print("Test de resta con cadena: ERROR")
except TypeError:
    print("Test de resta con cadena: OK")