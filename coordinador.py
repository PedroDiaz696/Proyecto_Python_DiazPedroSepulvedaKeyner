import json

with open("registros_campers_350.json", "r", encoding="utf-8") as archivo:
    campers = json.load(archivo)

with open("trainers.json","r", encoding="utf-8") as archivoT:
     trainers = json.load(archivoT)

with open("usuariosCampus.json","r", encoding="utf-8") as archivoU:
     usuariosCampus = json.load(archivoU)

with open("rutas.json","r", encoding="utf-8") as archivo:
     rutas = json.load(archivo)

matriculas = []

# ─────────────────────────────────────────────
# guardar archivos
# ─────────────────────────────────────────────

def guardarCampers(campers):
    with open("registros_campers_350.json", "w", encoding="utf-8") as archivo:
        json.dump(campers, archivo, ensure_ascii=False, indent=2)

def guardarTrainers(trainers):
    with open("trainers.json", "w", encoding="utf-8") as archivoT:
        json.dump(trainers, archivoT, ensure_ascii=False, indent=4)

# ─────────────────────────────────────────────
# MENU CAMPERS
# ─────────────────────────────────────────────

def mostrarCampers(campers):
    print("\n--- LISTADO DE CAMPERS ---")
    for c in campers:
        print(f"ID: {c['# de identificacion']} | Nombre: {c['nombre']} {c['apellido']} | Estado: {c['estado']['situacion']} | Grupo: {c['grupo']}")

def actualizarCamper(campers):
    idBuscar = input("ID del camper a actualizar: ").strip()
    for camper in campers:
        if camper["# de identificacion"] == idBuscar:
            print(f"Camper encontrado: {camper['nombre']} {camper['apellido']}")
            print("¿Qué deseas actualizar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Dirección")
            print("4. Correo")
            print("5. Grupo")
            print("6. Jornada")
            print("7. Estado (situacion)")
            print("8. En riesgo")
            op = input("Opción: ").strip()
            if op == "1":
                camper["nombre"] = input("Nuevo nombre: ").strip()
            elif op == "2":
                camper["apellido"] = input("Nuevo apellido: ").strip()
            elif op == "3":
                camper["direccion"] = input("Nueva dirección: ").strip()
            elif op == "4":
                camper["correo"] = input("Nuevo correo: ").strip()
            elif op == "5":
                camper["grupo"] = input("Nuevo grupo: ").strip()
            elif op == "6":
                camper["jornada"] = input("Nueva jornada: ").strip()
            elif op == "7":
                camper["estado"]["situacion"] = input("Nueva situacion (Inscrito/Cursando/Graduado/Retirado/Expulsado): ").strip()
            elif op == "8":
                camper["estado"]["en riesgo"] = input("¿En riesgo? (si/no): ").strip().lower()
            else:
                print("Opción inválida")
                return
            guardarCampers(campers)
            print("Camper actualizado correctamente.")
            return
    print("Camper no encontrado.")

def eliminarCamper(campers):
    idBuscar = input("ID del camper a eliminar: ").strip()
    for i, camper in enumerate(campers):
        if camper["# de identificacion"] == idBuscar:
            confirmacion = input(f"¿Seguro que deseas eliminar a {camper['nombre']} {camper['apellido']}? (s/n): ").strip().lower()
            if confirmacion == "s":
                campers.pop(i)
                guardarCampers(campers)
                print("Camper eliminado.")
            else:
                print("Operación cancelada.")
            return
    print("Camper no encontrado.")

def menuCampers(campers):
    while True:
        print("\n--- MENU CAMPERS ---")
        print("1. Mostrar campers")
        print("2. Actualizar camper")
        print("3. Eliminar camper")
        print("4. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            mostrarCampers(campers)
        elif op == "2":
            actualizarCamper(campers)
        elif op == "3":
            eliminarCamper(campers)
        elif op == "4":
            break
        else:
            print("Opción inválida.")

# ─────────────────────────────────────────────
# MENU TRAINERS
# ─────────────────────────────────────────────

def crearTrainer(trainers):
    print("\n--- MENU TRAINER ---")
    nuevoId = str(len(trainers) + 1)
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    horaInicio = input("Hora de inicio (ej: 6 AM): ").strip()
    horaFin = input("Hora fin (ej: 2 PM): ").strip()
    especialidad = input("Especialidad: ").strip()
    grupo1 = input("Grupo 1: ").strip()
    grupo2 = input("Grupo 2: ").strip()
    grupo3 = input("Grupo 3 (o 'no existe'): ").strip()

    nuevoTrainer = {
        "id": nuevoId,
        "nombre": nombre,
        "correo": correo,
        "hora de inicio": horaInicio,
        "hora fin": horaFin,
        "especialidad": especialidad,
        "grupo1": grupo1,
        "grupo2": grupo2,
        "grupo3": grupo3
    }
    trainers.append(nuevoTrainer)
    guardarTrainers(trainers)
    print("Trainer creado correctamente.")

def mostrarTrainers(trainers):
    print("\n--- LISTADO DE TRAINERS ---")
    for t in trainers:
        print(f"ID: {t['id']} | Nombre: {t['nombre']} | Correo: {t['correo']} | Especialidad: {t['especialidad']} | Grupos: {t['grupo1']}, {t['grupo2']}, {t['grupo3']}")

def actualizarTrainer(trainers):
    idBuscar = input("ID del trainer a actualizar: ").strip()
    for trainer in trainers:
        if trainer["id"] == idBuscar:
            print(f"Trainer encontrado: {trainer['nombre']}")
            print("¿Qué deseas actualizar?")
            print("1. Nombre")
            print("2. Correo")
            print("3. Hora de inicio")
            print("4. Hora fin")
            print("5. Especialidad")
            print("6. Grupo 1")
            print("7. Grupo 2")
            print("8. Grupo 3")
            op = input("Opción: ").strip()
            if op == "1":
                trainer["nombre"] = input("Nuevo nombre: ").strip()
            elif op == "2":
                trainer["correo"] = input("Nuevo correo: ").strip()
            elif op == "3":
                trainer["hora de inicio"] = input("Nueva hora de inicio: ").strip()
            elif op == "4":
                trainer["hora fin"] = input("Nueva hora fin: ").strip()
            elif op == "5":
                trainer["especialidad"] = input("Nueva especialidad: ").strip()
            elif op == "6":
                trainer["grupo1"] = input("Nuevo grupo 1: ").strip()
            elif op == "7":
                trainer["grupo2"] = input("Nuevo grupo 2: ").strip()
            elif op == "8":
                trainer["grupo3"] = input("Nuevo grupo 3: ").strip()
            else:
                print("Opción inválida")
                return
            guardarTrainers(trainers)
            print("Trainer actualizado correctamente.")
            return
    print("Trainer no encontrado.")

def eliminarTrainer(trainers):
    idBuscar = input("ID del trainer a eliminar: ").strip()
    for i, trainer in enumerate(trainers):
        if trainer["id"] == idBuscar:
            confirmacion = input(f"¿Seguro que deseas eliminar a {trainer['nombre']}? (s/n): ").strip().lower()
            if confirmacion == "s":
                trainers.pop(i)
                guardarTrainers(trainers)
                print("Trainer eliminado.")
            else:
                print("Operación cancelada.")
            return
    print("Trainer no encontrado.")

def menuTrainers(trainers):
    while True:
        print("\n--- MENU TRAINERS ---")
        print("1. Crear trainer")
        print("2. Mostrar trainers")
        print("3. Actualizar trainer")
        print("4. Eliminar trainer")
        print("5. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            crearTrainer(trainers)
        elif op == "2":
            mostrarTrainers(trainers)
        elif op == "3":
            actualizarTrainer(trainers)
        elif op == "4":
            eliminarTrainer(trainers)
        elif op == "5":
            break
        else:
            print("Opción inválida.")

# ─────────────────────────────────────────────
# EXAMEN INICIAL
# ─────────────────────────────────────────────

def registrarExamenInicial(campers):
    idBuscar = input("# de identificacion del camper: ").strip()
    for camper in campers:
        if camper["# de identificacion"] == idBuscar:
            teoria = float(input("Nota teorica: "))
            practica = float(input("Nota practica: "))
            promedio = round((teoria + practica) / 2, 2)

            examen = {
                "nota teorica": teoria,
                "nota practica": practica,
                "promedio": promedio
            }

            if "examen inicial" not in camper:
                camper["examen inicial"] = {}
            camper["examen inicial"] = examen

            if promedio >= 60:
                camper["estado"]["situacion"] = "Aprobado"
                print(f"Camper aprobado con promedio: {promedio}")
            else:
                camper["estado"]["situacion"] = "Inscrito"
                print(f"Camper no aprobado. Promedio: {promedio}")

            guardarCampers(campers)
            return
    print("Camper no encontrado")

# ─────────────────────────────────────────────
# MATRICULA
# ─────────────────────────────────────────────

def matricularCampus(campers, rutas, matriculas):
    idBuscar = input("# de identificacion: ").strip()
    for camper in campers:
        if camper["# de identificacion"] == idBuscar:
            if camper["estado"]["situacion"] != "Aprobado":
                print("El camper no está aprobado")
                return
            for ruta in rutas:
                print("-", ruta["modulos"])
            nombreRuta = input("Ruta: ").strip()
            for ruta in rutas:
                if ruta["modulos"] == nombreRuta:
                    if len(ruta["campers"]) < ruta["capacidad"]:
                        ruta["campers"].append(camper["# de identificacion"])
                        camper["ruta"] = nombreRuta
                        camper["estado"]["situacion"] = "Cursando"
                        matricula = {
                            "camper": camper["# de identificacion"],
                            "ruta": nombreRuta,
                            "trainer": ruta["trainer"],
                            "fecha inicio": input("Fecha inicio: "),
                            "fecha fin": input("Fecha fin: "),
                            "salon": input("Salón: ")
                        }
                        matriculas.append(matricula)
                        guardarCampers(campers)
                        with open("rutas.json", "w", encoding="utf-8") as archivo:
                            json.dump(rutas, archivo, ensure_ascii=False, indent=4)
                        print("Camper matriculado")
                    else:
                        print("Ruta llena")
                    return
            print("Ruta no encontrada")
            return
    print("Camper no encontrado")

# ─────────────────────────────────────────────
# REPORTES
# ─────────────────────────────────────────────

def guardarReporte(tipo, filtro, resultados):
    try:
        with open("reportes.json", "r", encoding="utf-8") as archivoR:
            reportesGuardados = json.load(archivoR)
    except FileNotFoundError:
        reportesGuardados = []

    reporte = {
        "tipo": tipo,
        "filtro": filtro,
        "total": len(resultados),
        "campers": [
            {
                "id": c["# de identificacion"],
                "nombre": c["nombre"],
                "apellido": c["apellido"],
                "grupo": c["grupo"],
                "estado": c["estado"]["situacion"]
            }
            for c in resultados
        ]
    }

    reportesGuardados.append(reporte)

    with open("reportes.json", "w", encoding="utf-8") as archivoR:
        json.dump(reportesGuardados, archivoR, ensure_ascii=False, indent=4)

    print(f"Reporte guardado en reportes.json ({len(resultados)} campers).")

def reportes(campers, trainers):
    while True:
        print("\n--- REPORTES ---")
        print("1. Campers por grupo")
        print("2. Campers por estado")
        print("3. Campers por jornada")
        print("4. Volver")
        op = input("Opción: ").strip()
        if op == "1":
            grupo = input("Nombre del grupo: ").strip()
            encontrados = [c for c in campers if c.get("grupo") == grupo]
            if encontrados:
                for c in encontrados:
                    print(f"- {c['nombre']} {c['apellido']} | Estado: {c['estado']['situacion']}")
                guardarReporte("por grupo", grupo, encontrados)
            else:
                print("No hay campers en ese grupo.")
        elif op == "2":
            estado = input("Estado (Inscrito/Cursando/Graduado/Retirado/Expulsado/Aprobado): ").strip()
            encontrados = [c for c in campers if c["estado"]["situacion"] == estado]
            if encontrados:
                for c in encontrados:
                    print(f"- {c['nombre']} {c['apellido']} | Grupo: {c['grupo']}")
                guardarReporte("por estado", estado, encontrados)
            else:
                print("No hay campers con ese estado.")
        elif op == "3":
            jornada = input("Jornada (mañana/tarde/noche): ").strip()
            encontrados = [c for c in campers if c.get("jornada") == jornada]
            if encontrados:
                for c in encontrados:
                    print(f"- {c['nombre']} {c['apellido']} | Grupo: {c['grupo']}")
                guardarReporte("por jornada", jornada, encontrados)
            else:
                print("No hay campers en esa jornada.")
        elif op == "4":
            break
        else:
            print("Opción inválida.")

# ─────────────────────────────────────────────
# CAMPERS EN RIESGO ALTO
# ─────────────────────────────────────────────

def verCampersEnRiesgo(campers):
    print("\n--- CAMPERS EN RIESGO ALTO ---")
    encontrados = False
    for camper in campers:
        if camper["estado"]["en riesgo"] == "si":
            print(f"- {camper['nombre']} {camper['apellido']} | ID: {camper['# de identificacion']} | Grupo: {camper['grupo']}")
            encontrados = True
    if not encontrados:
        print("No hay campers en riesgo alto.")

# ─────────────────────────────────────────────
# MENU COORDINADOR
# ─────────────────────────────────────────────

def menuCoordinador(correo):

    while True:

        with open("registros_campers_350.json", "r", encoding="utf-8") as archivo:
            campers = json.load(archivo)

        with open("trainers.json", "r", encoding="utf-8") as archivoT:
            trainers = json.load(archivoT)

        with open("rutas.json", "r", encoding="utf-8") as archivo:
            rutas = json.load(archivo)

        print("\n --- MENU COORDINADOR ---")
        print("1. MENU Campers")
        print("2. MENU Trainers")
        print("3. Examen Inicial")
        print("4. Matricula")
        print("5. Reportes")
        print("6. Ver campers en riesgo alto")
        print("7. Salir")

        op = input("Opción: ").strip()

        if op == "1":
            menuCampers(campers)

        elif op == "2":
            menuTrainers(trainers)

        elif op == "3":
            registrarExamenInicial(campers)

        elif op == "4":
            matricularCampus(campers, rutas, matriculas)

        elif op == "5":
            reportes(campers, trainers)

        elif op == "6":
            verCampersEnRiesgo(campers)

        elif op == "7":
            break

        else:
            print("Opción inválida.")