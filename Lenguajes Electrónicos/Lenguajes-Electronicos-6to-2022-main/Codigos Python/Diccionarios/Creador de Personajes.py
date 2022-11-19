# dic = {
#     "Characters":{
#         "Persona":{
#             "Nombre": "bau",
#             "Apellido": "ASD"
#         }
#     }
# }
dic = {
    "Characters":{}
}
def CharacterDataInput(dec):
    for i in range(dec):
        dic["Characters"][f"Persona {i}"] = {}
        dic["Characters"][f"Persona {i}"]["Nombre"] = input("Ingrese el nombre: ")
        dic["Characters"][f"Persona {i}"]["Apellido"] = input("Ingrese el apellido: ")
        dic["Characters"][f"Persona {i}"]["Clase"] = input("Ingrese la clase---Clases disponibles:\n- Mago\n- Healer\n- Barbaro\n- Archer\n- ArtistaMarcial\n")
        dic["Characters"][f"Persona {i}"]["Altura"] = int(input("Ingrese la altura: "))
        dic["Characters"][f"Persona {i}"]["Peso"] = int(input("Ingrese el peso: "))
        i+=1
        print(i)
        
    

def CharacterView():
    decision1 = input("¿Desea ver los datos de un personaje en especifico?Escriba el nombre siendo el caso y No si no es el caso\n")
    if decision1 == "No":
        for i in dic["Characters"]:
            print(dic["Characters"][i]["Nombre"])
    else:
        for i in dic["Characters"]:
            if dic["Characters"][i]["Nombre"] == decision1:
                print(dic["Characters"][i])

while (1):
    decision = input("Bienvenido a la creacion de personajes\n¿Que desea hacer?\nEscriba Creacion si desea crear un personaje, Ver si desea ver los personajes guardados o Cerrar si desea finalizar el Creador de personajes\n")
    if decision == "Creacion":
        decision3= int(input("Ingrese la cantidad de personajes que desea crear\n"))
        CharacterDataInput(decision3)
    elif decision == "Ver":
        CharacterView()
    elif decision == "Cerrar":
        break