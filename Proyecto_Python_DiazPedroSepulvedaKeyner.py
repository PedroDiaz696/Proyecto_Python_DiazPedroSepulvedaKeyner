#git push origin main "subir los cambios a la nube"


import json

with open("registros_campers_350.json", "r", encoding="utf-8") as archivo: #open = abre el archivo #,"r", para read/leer #"utf-8" = para que no falle con tildes #"as archivo" variable que representa el archivo #with abre el archivo y lo cierra automaticamente
    campers = json.load(archivo) #json.load() sirve para que pase el archivo json a python

with open("trainers.json","r", encoding="utf-8") as archivoT:
     trainers = json.load(archivoT)

with open("usuariosCampus.json","r", encoding="utf-8") as archivoU:
     usuariosCampus = json.load(archivoU)

with open("rutas.json","r", encoding="utf-8") as archivo:
     rutas = json.load(archivo)

from camper import menuCampers
from trainer import menuTrainer
from coordinador import menuCoordinador

def menuGeneral():
    
    while True:
        print("--- BIENVENIDO A CAMPUSLANDS ---")
        print("\n1. iniciar sesion")
        print("2. salir")
        opmenuG = int(input(": "))
        if opmenuG == 1:
            menuInicioSesion()
        elif opmenuG == 2:
            break




def menuInicioSesion():
    print("")
    print("------------------------------")
    print("------- INICIAR SESION -------")
    print("------------------------------")
    print("")
    correo = input("ingresa tu correo: ")
    contraseña = input("ingresa tu contraseña: ")
    for usucamp in usuariosCampus:
        if correo.strip().lower() == usucamp["correo"].strip().lower() and contraseña.strip() == usucamp["contraseña"]: #.strip() para evitar errores por espacios al inicio o al final y .lower() para evitar errores por mayusculas
            if usucamp["rol"] == "camper":
                menuCampers(correo) #el (correo) es la informacion que envia a la funcion
            elif usucamp["rol"] == "trainer":
                menuTrainer(correo)
            elif usucamp["rol"] == "coordinador":
                menuCoordinador(correo)
            return #sale de la funcion / en este caso cuando se coloca un correo o contraseña incorrectos, vuelve al menu del inicio
    print("\n nombre o contraseña incorrectos!")
    print("")
     



menuGeneral()



