def registrarExamenInicial():
    id_buscar = input("ID del camper: ")

    for camper in campers:
        if camper["id"] == id_buscar:
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



def registrarExamenInicial():
    id_buscar = input("ID del camper: ")

    for camper in campers:
        if camper["id"] == id_buscar:
            teoria = float(input("Nota teorica: "))

            practica = float(input("Nota practica: "))

            promedio = (teoria + practica) / 2

                if promedio >=60:
                    camper["estado"] = "Aprobado"
                    print("Camper aprobado")
                else:
                    print("Camper no aprobado")
                return
            
            print("Camper no encontrado")

def asignarRutaTrainer():
    for r in rutas:
        print("-", r["nombre"])

    nombre_ruta = input("Ruta: ")

    for ruta in rutas:
        if ruta["nombre"] == nombre_ruta:

            for t in trainers:
                print("-", t["nombre"])
            
            nombre_trainer = input("Trainer: ")

            ruta["trainer"] = nombre_trainer
            print("Trainer asignado")
            return
        

with open("coordinador.json", "r", encoding="utf-8") as archivo:
     coordinador = json.load(archivo)