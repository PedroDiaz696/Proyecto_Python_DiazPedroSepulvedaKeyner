import json

with open("registros_campers_350.json", "r", encoding="utf-8") as archivo: #open = abre el archivo #,"r", para read/leer #"utf-8" = para que no falle con tildes #"as archivo" variable que representa el archivo #with abre el archivo y lo cierra automaticamente
    campers = json.load(archivo) #json.load() sirve para que pase el archivo json a python

with open("trainers.json","r", encoding="utf-8") as archivoT:
     trainers = json.load(archivoT)

with open("usuariosCampus.json","r", encoding="utf-8") as archivoU:
     usuariosCampus = json.load(archivoU)

with open("rutas.json","r", encoding="utf-8") as archivo:
     rutas = json.load(archivo)

matriculas = []

def registrarExamenInicial(campers):
    
        idBuscar = input("# de identificacion del camper: ")

        for camper in campers:
                if camper["# de identificacion"] == idBuscar:
                        teoria = float(input("Nota teorica: "))

                        practica = float(input("Nota practica: "))

                        promedio = (teoria + practica) / 2

                        if promedio >= 60:
                                camper["estado"] = "Aprobado"
                                print("Camper aprobado")
                        else:
                                print("Camper no aprobado")
                        return
            

        print("Camper no encontrado")

def asignarRutaTrainer(rutas, trainers):
    for r in rutas:
        print("-", r["nombre"])

    nombreRuta = input("Ruta: ")

    for ruta in rutas:
        if ruta["nombre"] == nombreRuta:

            for t in trainers:
                print("-", t["nombre"])
            
            nombreTrainer = input("Trainer: ")

            ruta["trainer"] = nombreTrainer
            print("Trainer asignado")
            return

def matricularCampus(campers, rutas, matriculas):
    idBuscar = input("ID camper: ")

    for camper in campers:

        if camper["id"] == idBuscar:

            if camper["estado"] == "Aprobado":
                
                print("El camper no está aprobado")

                return

            for ruta in rutas:
                print("-", ruta["nombre"])

            nombreRuta = input("Ruta: ")
            
            for ruta in rutas:

                if ruta["nombre"] == nombreRuta:

                    if len(ruta["campers"]) < ruta["capacidad"]:
                        ruta["campers"].append(camper["id"])
                        camper["ruta"] = nombreRuta
                        camper["estado"] = "Cursando"

                        matricula = {
                                "camper": camper["id"],
                                "ruta": nombreRuta,
                                "trainer": ruta["trainer"],
                                "fecha inicio": input("Fecha inicio: "),
                                "fecha fin": input("Fecha fin: "),
                                "salon": input("Salón: ")
                            }
                        matriculas.append(matricula)

                        print("Camper matriculado")
                        
                else:

                        print("Ruta llena")

                return

def evaluarModulo(campers):

    idBuscar = input("ID camper: ")

    for camper in campers:

        if camper["id"] == idBuscar:

            teoria = float(input("Teoria: "))
            practica = float(input("Práctica: "))
            quiz = float(input("Quices: "))

            notaFinal = teoria*0.3 + practica*0.6 + quiz*0.1

            camper["notas"].append(notaFinal)

            if notaFinal < 60:
                camper["riesgo"] = True
                print("Camper en riesgo")
            else:
                print("Módulo aprobado")
            return

def reporteRiesgo(campers):

    print("\n--- CAMPERS EN RIESGO ---")

    for camper in campers:
        if camper["riesgo"]:
            print(camper["nombres"], camper["apellidos"])

def matricularCamper(camper, grupo):
    grupo["campers"].append(camper)

def menuCoordinador(correo):

    while True:

        print("\n--- MENU COORDINADOR ---")
        print("1. Registrar examen inicial")
        print("2. Asignar trainer a ruta")
        print("3. Matricular camper")
        print("4. Evaluar módulo")
        print("5. Ver campers en riesgo")
        print("0. salir")
        
        op = input("Opción: ")

        if op == "1":
            registrarExamenInicial(campers)

        elif op == "2":
            asignarRutaTrainer(rutas, trainers)

        elif op == "3":
            matricularCampus(campers, rutas, matriculas)

        elif op == "4":
            evaluarModulo(campers)

        elif op == "5":
            reporteRiesgo(campers)

        elif op == "0":
            break


    


