censo_2017 = {
    "14": {
        "Nombre_región": "Los Rios",
        "Superficie" : int(18429),
        "habitantes" : 404432
        },
    "12": {
        "Nombre_región": "Magallanes",
        "Superficie" : int(1382291),
        "habitantes" : int(166533)
        }
}
print(f"Diccionario inicial: \n {censo_2017}\n ")

densidad14 = float(round(censo_2017["14"]["habitantes"] /censo_2017["14"]["Superficie"]))
densidad12 = float(round(censo_2017["12"]["habitantes"] /censo_2017["12"]["Superficie"]))

censo_2017["14"]["densidad"]= densidad14 # se agrega clave densidad y valor a diccionario
censo_2017["12"]["densidad"]= densidad12 # se agrega clave densidad y valor a diccionario

censo_2017["14"]["Capital"] = "Valdivia"
censo_2017["14"]["Comunas"] = ["Rio Bueno", "La Union", "Paillaco"]
censo_2017["14"]["Coordenadas_simuladas"] = (-39.8,-73.2)
censo_2017["14"]["Zonas_exclusivas"] = {"Urbana","Rural","Fronteriza"}

censo_2017["12"]["Capital"] = "Punta Arenas"
censo_2017["12"]["Comunas"] = ["Cabo de Hornos", "Puerto Williams", "Porvenir"]
censo_2017["12"]["Coordenadas_simuladas"] = (-59.9,-90.2)
censo_2017["12"]["Zonas_exclusivas"] = {"Urbana","Rural","Fronteriza"}

censo_2017["12"]["Nombre_región"] = "Magallanes y Antártica Chilena" 

while True:
    region = input("Ingrese el ID de la region para revisar sus comunas (12 o 14)\nSi desea salir escriba 'salir' o 0: ")
    
    if region == "salir" or region == "0":
        print("¡Hasta luego!")
        break
        
    elif region == "12":
        nombre = censo_2017['12']['Nombre_región']
        comunas = censo_2017['12']['Comunas']
        print(f"El id {region} corresponde a la region de {nombre},\nsus comunas son {comunas}\n")
        
    elif region == "14":
        nombre = censo_2017['14']['Nombre_región']
        comunas = censo_2017['14']['Comunas']
        print(f"El id {region} corresponde a la region de {nombre},\nsus comunas son {comunas}\n")
        
    else:
        print("ID de región no válido. Intente nuevamente.\n")

print(f"Las claves del diccionario final son: {censo_2017.items()}")






