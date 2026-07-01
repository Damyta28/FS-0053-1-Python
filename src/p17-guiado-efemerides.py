
efemerides = {
    "1 enero": "Año Nuevo",
    "27 febrero": "Terremoto en Chile (2010)",
    "8 marzo": "Día Internacional de la Mujer",
    "21 mayo": "Glorias Navales de Chile",
    "18 septiembre": "Fiestas Patrias de Chile",
    "19 septiembre": "Glorias del Ejército de Chile",
    "25 diciembre": "Navidad"
}

for clave, valor in efemerides.items():
    efemerides[clave.lower().strip()] = valor

fecha = input("Ingrese una fecha (formato: día mes): ")

fecha_buscar = fecha.lower().strip()

efe = efemerides.get(fecha_buscar, "ND")

if efe == "ND": 
    print("No hay efemérides para esta fecha.")
    print(f"Efemérides para {fecha}: {efe}")
else:
    print(f"Efemérides para {fecha}: {efe}")    

    
