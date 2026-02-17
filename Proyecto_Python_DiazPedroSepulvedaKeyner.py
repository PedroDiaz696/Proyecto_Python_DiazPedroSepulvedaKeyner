#git push origin main "subir los cambios a la nube"


import json

with open("registros_campers_350.json", "r", encoding="utf-8") as archivo: #open = abre el archivo #,"r", para read/leer #"utf-8" = para que no falle con tildes #"as archivo" variable que representa el archivo #with abre el archivo y lo cierra automaticamente
    campers = json.load(archivo) #json.load() sirve para que pase el archivo json a python

with open("trainers.json","r", encoding="utf-8") as archivoT:
     trainers = json.load(archivoT)

with open("usuariosCampus.json","r", encoding="utf-8") as archivoU:
     usuariosCampus = json.load(archivoU)

with open("grupos.json","r", encoding="utf-8") as archivo:
    grupos = json.load(archivo)

with open("rutas.json","r", encoding="utf-8") as archivo:
    rutas = json.load(archivo)

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
        elif opmenuG == 3:
            break


def menuRegistro():
    while True:

        print("")
        print("--------------------------")
        print("------- REGISTRATE -------")
        print("--------------------------")
        print("")
        correoRegistro = input("ingresa tu correo (@camper.com): ").strip() 
        if not correoRegistro.endswith("@camper.com"):    #para verificar si el correo termina en @camper.com
            print("¡El correo debe terminar en @camper.com!")
            return

        correo_existe = False
        for usuario in usuariosCampus:
            if usuario["correo"].strip().lower() == correoRegistro.lower():
                correo_existe = True
                break
        if correo_existe:
            print("¡este correo ya esta registrado!")
            continue

        break #termina con el ciclo si el correo no existe todavia y esta disponible

    while True:
        contraseñaRegistro = input("ingresa tu contraseña: ")
        confirmarcont = input("confirma tu contraseña")
        if contraseñaRegistro != confirmarcont:  #el != se usa para decir: "si no es igual a:"
            print("las contraseñas no coinciden, intentalo de nuevo")
            return
        break #rompe el ciclo cuando la contraseña es valida

    nuevo_usuario = {
        "correo": correoRegistro,
        "contraseña": contraseñaRegistro,
        "rol": "camper"
    }
    usuariosCampus.append(nuevo_usuario)

    with open("usuariosCampus.json","w", encoding="utf-8") as archivo:
        json.dump(usuariosCampus, archivo)

    print("\nREGISTRO EXITOSO")
    print("\nYa puedes iniciar sesion!")

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
     
def menuTrainer(correo):
    for trainer in trainers:
        if trainer["correo"].strip().lower() == correo.strip().lower(): #si el correo que se ingreso es = al de un trainer:
            trainer_actual = trainer #guarda la informacion del trainer para saber de quien se trata
            break #sale del bucle apenas se cumpla
    print("--- BIENVENIDO TRAINER ---")
    print("1. Asignar notas")
    print("2. Mirar estudiantes de su grupo")
    print("3. Salir")
    opTrainer = int(input(": "))
    if opTrainer == 1:
        asignarNotas(trainer_actual)
    elif opTrainer == 2:
        verEstudiantesTrainer(trainer_actual)
    elif opTrainer == 3:
        print("Saliendo...")
        return
    
def verEstudiantesTrainer(trainer_actual):
    print("")
    print(f"ESTUDIANTES DEL TRAINER: {trainer_actual['nombre']}")
    print("")


    
    #verificar que el trainer tenga grupos asignados
    if 'grupo' not in trainer_actual or not trainer_actual['grupo']:
        print("\neste trainer no tiene grupos asignados.")
        return

    #obtener los grupos del trainer (pueden ser varios separados por coma)
    grupos_trainer = [g.strip() for g in trainer_actual["grupo"].split(",")] #el .split(",") lo que hace es dividir por comas
    
    
    print(f"\nGrupos asignados: {', '.join(grupos_trainer)}")
    print(f"Especialidad: {trainer_actual.get('especialidad')}")
    print(f"Horario: {trainer_actual.get('hora de inicio')} - {trainer_actual.get('hora fin')}")
    
    codigo = ""

    def obtenerEstudiantesGrupo():
        for g in grupos:
            if g["codigo"] == codigo:
                return g["campers"]
        return[]
    
    #mostrar estudiantes por cada grupo
    for codigo_grupo in grupos_trainer:
        print("")
        print(f"GRUPO: {codigo_grupo}")
        print("")
        
        estudiantes_grupo = obtenerEstudiantesGrupo(codigo_grupo)
        
        if not estudiantes_grupo:
            print(f"  No hay estudiantes asignados a este grupo aún.")
            print(f"  El coordinador debe asignar grupos primero.")
        else:
            #buscar información del grupo
            grupo_info = None
            for g in grupos:
                if g.get('codigo') == codigo_grupo:
                    grupo_info = g
                    break
            
            if grupo_info:
                print(f"  Jornada: {grupo_info.get('jornada', 'N/A')}")
                print(f"  Total de estudiantes: {len(estudiantes_grupo)}")
            
            #separar por estado
            cursando = [e for e in estudiantes_grupo if e['estado']['situacion'] == 'Cursando']
            otros = [e for e in estudiantes_grupo if e['estado']['situacion'] != 'Cursando']
            
            #mostrar estudiantes cursando
            if cursando:
                print(f"\nESTUDIANTES CURSANDO ({len(cursando)}):")
                for i, estudiante in enumerate(cursando, 1):
                    en_riesgo = "EN RIESGO" if estudiante['estado'].get('en riesgo') == 'si' else ""
                    print(f"    {i:2d}. {estudiante['nombre']:<15} {estudiante['apellido']:<15} | ID: {estudiante['# de identificacion']}{en_riesgo}")
            
            #mostrar otros estados
            if otros:
                print(f"\nOTROS ESTADOS ({len(otros)}):")
                estados_dict = {}
                for e in otros:
                    estado = e['estado']['situacion']
                    if estado not in estados_dict:
                        estados_dict[estado] = []
                    estados_dict[estado].append(e)
                
                for estado, estudiantes in estados_dict.items():
                    print(f"\n    {estado}: {len(estudiantes)} estudiantes")
                    for est in estudiantes[:3]:  # Mostrar solo los primeros 3
                        print(f"      • {est['nombre']} {est['apellido']}")
                    if len(estudiantes) > 3:
                        print(f"      ... y {len(estudiantes) - 3} más")
        


modulos = [
    "fundamentos de programacion",
    "programacion web",
    "programacion formal",
    "bases de datos",
    "backend"
]


def asignarNotas(trainer_actual):
    nombreEstudianteasignar = input("ingrese el nombre del estudiante: ").strip()
        
    print("\n--- MODULOS ---")
    nombre = input("Nombre del estudiante: ").strip()

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
        "nombre": nombre,
        "modulo": moduloSeleccionado,
        "notas": {
            "nota practica": practica,
            "nota teorica": teorica,
            "nota trabajos": trabajos,
            "nota final": round(notaFinal, 2)
        }
    }

    guardarNotas(registro)
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
            with open("notas.json", "r", encoding="utf-8") as archivo:
                notas = json.load(archivo)
                
                # Verificar si el archivo tiene contenido
            if not notas or len(notas) == 0:
                print("\nEl sistema de notas esta vacio")
                print("Aún no hay notas registradas para ningún estudiante")
                print("Un trainer debe asignar las notas primero")
            else:
                    # Buscar notas del camper actual
                notas_encontradas = False
                for nota in notas:
                    if nota["nombre"].strip().lower() == camper_actual["nombre"].strip().lower():
                        notas_encontradas = True
                        print(f"\n Módulo: {nota['modulo']}") #f sirve para que lo que esta adentro de las "" se lea bien, por ejemplo los {}
                        print(f"   -Nota práctica (60%): {nota['notas']['nota practica']}")
                        print(f"   -Nota teórica (30%): {nota['notas']['nota teorica']}")
                        print(f"   -Nota trabajos (10%): {nota['notas']['nota trabajos']}")
                        print(f"   -Nota final: {nota['notas']['nota final']}")
                    
                if notas_encontradas == False: #notas_encontradas = false
                    print(f"\n No tienes notas registradas aún.")
                    print(f"Tu trainer asignará tus calificaciones próximamente.")
                    

        elif opcionCamper == 3:
            
            grupo_estudiante = camper_actual['# de identificacion']
            
            if grupo_estudiante:
                print(f"Grupo asignado: {grupo_estudiante['codigo']}")
                print(f"Jornada: {grupo_estudiante['jornada']}")
            else:
                print("Aún no tienes un grupo asignado.")

        elif opcionCamper == 4:
            print("Saliendo del menú camper...")
            break

matriculas = []

def registrarExamenInicial():
    
        idBuscar = input("ID del camper: ")

        for camper in campers:
                if camper["id"] == idBuscar:
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

def asignarRutaTrainer():
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

def matricularCampus():
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

def evaluarModulo():

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

def reporteRiesgo():

    print("\n--- CAMPERS EN RIESGO ---")

    for camper in campers:
        if camper["riesgo"]:
            print(camper["nombres"], camper["apellidos"])

def matricularCamper(camper, grupo):
    grupo["campers"].append(camper)

def menuCoordinador():

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
            matricularCamper(campers, rutas, matriculas)

        elif op == "4":
            evaluarModulo(campers)

        elif op == "5":
            reporteRiesgo(campers)

        elif op == "0":
            break


    




menuGeneral()



