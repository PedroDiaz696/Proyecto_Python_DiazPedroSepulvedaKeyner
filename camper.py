import json

with open("registros_campers_350.json", "r", encoding="utf-8") as archivo: #open = abre el archivo #,"r", para read/leer #"utf-8" = para que no falle con tildes #"as archivo" variable que representa el archivo #with abre el archivo y lo cierra automaticamente
    campers = json.load(archivo) #json.load() sirve para que pase el archivo json a python

with open("usuariosCampus.json","r", encoding="utf-8") as archivoU:
     usuariosCampus = json.load(archivoU)

def menuCampers(correo):  #recibe el correo del camper 
    with open("registros_campers_350.json", "r", encoding="utf-8") as archivo:  ##se vuelven a pedri para que este la informacion actualizada
        campers = json.load(archivo)
    
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
            

        elif opcionCamper == 2:

            print("\n--- MIS NOTAS ---")

            if "notas" not in camper_actual or len(camper_actual["notas"]) == 0:
                print("\nAún no tienes notas registradas")
                print("Un trainer debe asignarlas primero")
            else:
                for nota in camper_actual["notas"]:
                    print(f"\n Módulo: {nota['modulo']}")
                    print(f"   -Nota práctica (60%): {nota['nota practica']}")
                    print(f"   -Nota teórica (30%): {nota['nota teorica']}")
                    print(f"   -Nota trabajos (10%): {nota['nota trabajos']}")
                    print(f"   -Nota final: {nota['nota final']}")
            
                    
                    

        elif opcionCamper == 3:
            print("")
            print("--- GRUPO ---")
            if 'grupo' in camper_actual:
                print(f"Grupo: {camper_actual['grupo']}")
                print(f"Jornada: {camper_actual['jornada']}")
            elif camper_actual["estado"]["situacion"] == "Retirado" or camper_actual["estado"]["situacion"] == "Expulsado":
                print("Ya no formas parte de CAMPUSLANDS!")
            elif camper_actual["estado"]["situacion"] == "Graduado":
                print("Ya estas graduado/a!")
            else:
                print("Aun no tienes un grupo asignado!")


        elif opcionCamper == 4:
            print("Saliendo del menú camper...")
            break