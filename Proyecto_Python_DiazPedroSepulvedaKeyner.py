#git push origin main "subir los cambios a la nube"


import json

with open("registros_campers_350.json", "r", encoding="utf-8") as archivo: #open = abre el archivo #,"r", para read/leer #"utf-8" = para que no falle con tildes #"as archivo" variable que representa el archivo #with abre el archivo y lo cierra automaticamente
    campers = json.load(archivo) #json.load() sirve para que pase el archivo json a python

with open("trainers.json","r", encoding="utf-8") as archivoT:
     trainers = json.load(archivoT)

with open("usuariosCampus.json","r", encoding="utf-8") as archivoU:
     usuariosCampus = json.load(archivoU)


def menuGeneral():
    
    while True:
        print("--- BIENVENIDO A CAMPUSLANDS ---")
        print("\n1. iniciar sesion")
        print("2. registrarme")
        print("3. salir")
        opmenuG = int(input(": "))
        if opmenuG == 1:
            menuInicioSesion()
        elif opmenuG == 2:
            menuRegistro()

    


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
                menuCoordinador()
            return #sale de la funcion / en este caso cuando se coloca un correo o contraseña incorrectos, vuelve al menu del inicio
    print("\n nombre o contraseña incorrectos!")
    print("")
     
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
        print(f"{i}. {modulo}")
        Mod = 1
        moduloSeleccionado = modulos[Mod-1]
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
    guardarNotas(registro)


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



        
def menuCampers(correo):  #recibe el correo del camper 
    camper_actual = None #indica que todavia no hay camper, es como cuando a una variable le ponemos = 0
    for camper in campers:
        if camper["correo"].strip().lower() == correo.strip().lower(): #si el correo que se ingreso es = al de un camper:
            camper_actual = camper #guarda la informacion del camper para saber de quien se trata
            break #sale del bucle apenas se cumpla
    
    while True:
        print("\n--- MENU CAMPER ---")
        print(f"Bienvenido/a {camper_actual['nombre']} {camper_actual['apellido']}")
        print("1. Ver estado de usuario")
        print("2. Ver notas")
        print("3. Ver grupo asignado")
        print("4. Salir")
        
        try:
            opcionCamper = int(input(": "))
        except ValueError: #para los errores de valor, por ejemplo un caracter cuando tiene que ingresar un numero
            print("opción invalida. ingrese un numero!")
            continue #por asi decirlo, invalida la opcion y la cierra

        if opcionCamper == 1:
            print("\n--- ESTADO DEL USUARIO ---")
            print(f"Nombre: {camper_actual['nombre']} {camper_actual['apellido']}") #f"" para que lea el {} como el valor que es, tal cual
            print(f"Identificacion: {camper_actual['# de identificacion']}")
            print(f"Estado: {camper_actual['estado']['situacion']}")
            
            if camper_actual['estado']['situacion'] == "Cursando":
                print(f"¿Estás en riesgo?: {camper_actual['estado']['en riesgo']}")
            
            if 'grupo' in camper_actual:
                print(f"Grupo: {camper_actual['grupo']}")
                print(f"Jornada: {camper_actual['jornada']}")

        elif opcionCamper == 2:
            
            print("\n--- MIS NOTAS ---")
            try:
                with open("notas.json", "r", encoding="utf-8") as archivoN:
                    notas = json.load(archivoN)
                
                notas_encontradas = False
                for nota in notas:
                    
                    if nota["nombre"].strip().lower() == camper_actual["nombre"].strip().lower():
                        notas_encontradas = True
                        print(f"\nMódulo: {nota['modulo']}")
                        print(f"  Nota práctica: {nota['notas']['nota practica']}")
                        print(f"  Nota teórica: {nota['notas']['nota teorica']}")
                        print(f"  Nota trabajos: {nota['notas']['nota trabajos']}")
                        print(f"  Nota final: {nota['notas']['nota final']}")
                
                if not notas_encontradas:
                    print("No tienes notas registradas aún.")
                    
            except FileNotFoundError:
                print("No hay notas registradas en el sistema.")

        elif opcionCamper == 3:
            
            print("\n--- MI GRUPO ---")
            if 'grupo' in camper_actual:
                print(f"Grupo asignado: {camper_actual['grupo']}")
                print(f"Jornada: {camper_actual['jornada']}")
                
                
                print(f"\nCompañeros del grupo {camper_actual['grupo']}:")
                contador = 0
                for compañero in campers:
                    if 'grupo' in compañero and compañero['grupo'] == camper_actual['grupo']:
                        if compañero['correo'] != camper_actual['correo']:  # No mostrar al usuario actual
                            contador += 1
                            print(f"  {contador}. {compañero['nombre']} {compañero['apellido']}")
            else:
                print("Aún no tienes un grupo asignado.")

        elif opcionCamper == 4:
            print("Saliendo del menú camper...")
            break


    




menuGeneral()



