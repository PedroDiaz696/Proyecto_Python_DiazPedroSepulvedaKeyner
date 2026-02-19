import json

with open("registros_campers_350.json", "r", encoding="utf-8") as archivo: #open = abre el archivo #,"r", para read/leer #"utf-8" = para que no falle con tildes #"as archivo" variable que representa el archivo #with abre el archivo y lo cierra automaticamente
    campers = json.load(archivo) #json.load() sirve para que pase el archivo json a python

with open("trainers.json","r", encoding="utf-8") as archivoT:
     trainers = json.load(archivoT)

with open("usuariosCampus.json","r", encoding="utf-8") as archivoU:
     usuariosCampus = json.load(archivoU)



def menuTrainer(correo):
    with open("registros_campers_350.json", "r", encoding="utf-8") as archivo:
        campers = json.load(archivo)
    with open("trainers.json", "r", encoding="utf-8") as archivoT:
        trainers = json.load(archivoT)

    for trainer in trainers:
        if trainer["correo"].strip().lower() == correo.strip().lower(): #si el correo que se ingreso es = al de un trainer:
            trainer_actual = trainer #guarda la informacion del trainer para saber de quien se trata
            break #sale del bucle apenas se cumpla

    while True:
        print("--- BIENVENIDO TRAINER ---")
        print("1. Asignar notas")
        print("2. Mirar estudiantes de sus grupo")
        print("3. Salir")
        opTrainer = int(input(": "))
        if opTrainer == 1:
            asignarNotas(trainer_actual)
        elif opTrainer == 2:
            verEstudiantesTrainer(trainer_actual, campers)
        elif opTrainer == 3:
            print("Saliendo...")
            break
    
def verEstudiantesTrainer(trainer_actual, campers):
    print("")
    print(f"ESTUDIANTES DEL TRAINER: {trainer_actual['nombre']}")
    print("")
    print("tus grupos son:")

    print(f"{trainer_actual.get('grupo1')}:")
    encontrados = False #dice que aun no hay estidiantes encontrados
    for grup in campers:
        if grup.get("grupo") in trainer_actual["grupo1"]:
            print(f"- {grup['nombre']}")
            encontrados = True #ya encontro al menos un estudiante, asi que sigue buscando hasta encontrar todos
    if not encontrados: #solo se ejecuta si encontrados sigue siendo false, lo que quiere decir que no hay estudiantes en ese grupo
        print("aun no tienes estudiantes en este grupo!")

    print(f"{trainer_actual.get('grupo2')}:")
    encontrados = False
    for gru in campers:
        if gru.get("grupo") in trainer_actual["grupo2"]:
            print(f"- {gru['nombre']}")
            encontrados = True
    if not encontrados:
        print("aun no tienes estudiantes en este grupo!")

    print(f"{trainer_actual.get('grupo3')}:")
    encontrados = False
    for gr in campers:
        if gr.get("grupo") in trainer_actual["grupo3"]:
            print(f"- {gr['nombre']}")
            encontrados = True
    if not encontrados:
        print("aun no tienes estudiantes en este grupo!")

    print(f"Especialidad: {trainer_actual.get('especialidad')}")
    print(f"Horario: {trainer_actual.get('hora de inicio')} - {trainer_actual.get('hora fin')}")



modulos = [
    "fundamentos de programacion",
    "programacion web",
    "programacion formal",
    "bases de datos",
    "backend"
]


def asignarNotas(trainer_actual):

    while True:

        nombreEstudianteasignar = input("\ningrese el # de identificacion del estudiante: ").strip()

        print("\n--- MODULOS ---")
        for i, modulo in enumerate(modulos, 1):
            print(f"{i}. {modulo}")

        opcion = int(input("Seleccione módulo: "))
        moduloSeleccionado = modulos[opcion - 1]

        practica = float(input("Nota práctica (60%): "))
        teorica = float(input("Nota teórica (30%): "))
        trabajos = float(input("Nota trabajos (10%): "))

        notaFinal = practica*0.6 + teorica*0.3 + trabajos*0.1

        registro = {
            "nombre": nombreEstudianteasignar,
            "modulo": moduloSeleccionado,
            "notas": {
                "nota practica": practica,
                "nota teorica": teorica,
                "nota trabajos": trabajos,
                "nota final": round(notaFinal, 2)
            }
        }

        guardarNotas(registro)

        continuar = input("\ndesea asignar otra nota? (s/n): ").lower()

        if continuar != "s":
            break


def guardarNotas(registro):

    with open("registros_campers_350.json", "r", encoding="utf-8") as archivoC:
        campers = json.load(archivoC)

    for camper in campers:
        if camper["# de identificacion"] == registro["nombre"]:

            if "notas" not in camper:
                camper["notas"] = []

            camper["notas"].append({
                "modulo": registro["modulo"],
                "nota practica": registro["notas"]["nota practica"],
                "nota teorica": registro["notas"]["nota teorica"],
                "nota trabajos": registro["notas"]["nota trabajos"],
                "nota final": registro["notas"]["nota final"]
            })

            break

    with open("registros_campers_350.json", "w", encoding="utf-8") as archivoC:
        json.dump(campers, archivoC, indent=4)

    print("Notas Guardadas!")