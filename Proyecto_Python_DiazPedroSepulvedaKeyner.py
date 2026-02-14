#git push origin main "subir los cambios a la nube"


import json

with open("registros_campers_350.json", "r", encoding="utf-8") as archivo: #open = abre el archivo #,"r", para read/leer #"utf-8" = para que no falle con tildes #"as archivo" variable que representa el archivo #with abre el archivo y lo cierra automaticamente
    campers = json.load(archivo) #json.load() sirve para que pase el archivo json a python

with open("trainers.json","r", encoding="utf-8") as archivoT:
     trainers = json.load(archivoT)

def menuRegistro():
    print("--------------------------")
    print("------- REGISTRATE -------")
    print("--------------------------")
    print("1. Camper")
    print("2. Trainer")
    print("3. Coordinador")
    opcionRegistro = int(input(": "))
    if opcionRegistro == 1:
        registroCamper()
    if opcionRegistro == 2: 
        registroTrainer()

def registroTrainer():
    nombreTrainer = input("cual es tu nombre? trainer: ")
    passwordTrainer = input("ingresa tu contraseña: ")
    for nombreT in trainers:
        if nombreTrainer.strip().lower() == nombreT["nombre"].strip().lower() and passwordTrainer.strip() == nombreT["password"]: #.strip() para evitar errores por espacios al inicio o al final y .lower() para evitar errores por mayusculas
            menuTrainer()
            return # sale de la funcion
    print("nombre o contraseña incorrectos!")
        
     
def menuTrainer():
    print("--- BIENVENIDO TRAINER ---")
    print("1. Asignar notas")
    print("2. Mirar estudiantes de su grupo")
    opTrainer = int(input(": "))
    if opTrainer == 1:
        asignarNotas()


modulos = [
    "fundamentos de programacion",
    "programacion web",
    "programacion formal",
    "bases de datos",
    "backend"
]


def asignarNotas():
    nombreEstudianteasignar = input("ingrese el nombre del estudiante: ").strip()
        
    print("\n--- MODULOS ---")
    for i, modulo in enumerate(modulos, start=1):
        print("{i}, {modulo}")
        elegirModulo = int(input("seleccione el modulo: "))
        moduloSeleccionado = modulos[elegirModulo-1]
        practica = float(input("nota prueba practica (60%): "))
        teorica = float(input("nota prueba teorica (30%): "))
        trabajos = float(input("nota final trabajos (10%): "))
        notaFinal = (practica*0.6) + (teorica*0.3) + (trabajos*0.1)
        
        registro = {
            "nombre": nombreEstudianteasignar,
            "modulo": moduloSeleccionado,
            "notas": {
                "nota practica": practica,
                "nota teorica": teorica,
                "nota trabajos": trabajos,
                "nota final": round(notaFinal, 2) #redondear numero a 2 decimales
            } 
                
        }
    


def guardarNotas(registro):
    try: #"intentar" por si el archivo no existe
        with open("notas.json","r", encoding="utf-8") as archivoN:
            notas = json.load(archivoN)
    except FileNotFoundError: #si el archivo no existe, en este caso crea una lista vacia
        notas = []

    notas.append(registro)
    with open("notas.json","w", encoding="utf-8") as archivoN:
        json.dump(notas, archivoN)
        print("Notas Guardadas!")


def registroCamper():
        print("--- Bienvenido Camper ---")
        print("Que quieres hacer? : ")
        print("1. Ver estado de usuario")
        print("3. ver lista de campers")
        opcionCamper = int(input(": "))

        if opcionCamper == 1:
            numeroIdentificacion = input("ingresa tu numero de identificacion :")
            for ni in campers:
                if ni["# de identificacion"] == numeroIdentificacion:
                     print("eres: ", ni["nombre"])
                     print("tu estado es: ", ni["estado"]["situacion"])
                     if ni["estado"]["situacion"] == "Cursando":
                          print("estas en riesgo? :",ni["estado"]["en riesgo"])
                     


        elif opcionCamper == 3:
             for listaCampers in campers:
                print(listaCampers["nombre"])




menuRegistro()



