import modules.utils as u


# ADMINS CRUD
def registro_eventos():
    eventos = u.leer_json("eventos.json")
    if eventos is None:
        eventos = []
    print(">>>>  Nuevo Evento <<<<<\n")
    id = input("ID Evento: ")
    nombre = input("Nombre: ")
    fecha = input("Fecha: ")
    hora = input("Hora: ")
    lugar = input("Lugar: ")
    capacidad = input("Aforo: ")

    nuevo_evento = {
        "id": id,
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "lugar": lugar,
        "capacidad": capacidad
    }
    eventos.append(nuevo_evento)
    u.escribir_json(eventos, "eventos.json")

    


def registro_artistas():
    pass

def monitorear_aforo():
    pass

# ADMINS REPORTES
def participacion_artistas():
    pass

def ver_proximos_eventos():
    pass

def listado_asistentes():
    pass

def eventros_menos_asistentes():
    pass

# ARTISTAS CRUD
def agenda_presentaciones():
    artista_id = input("Ingrese su ID de artista: ")
    asignaciones = u.leer_json("asignaciones_artistas.json")
    if asignaciones is None or len(asignaciones) == 0:
        print("No hay asignaciones de presentaciones.")
        return
    mis_asignaciones = [a for a in asignaciones if a['artista_id'] == artista_id]
    if len(mis_asignaciones) == 0:
        print("No tiene presentaciones asignadas.")
        return
    eventos = u.leer_json("eventos.json")
    if eventos is None:
        print("No hay eventos disponibles.")
        return
    print(">>>> Agenda de Presentaciones <<<<<")
    for asignacion in mis_asignaciones:
        evento = next((e for e in eventos if e['id'] == asignacion['evento_id']), None)
        if evento:
            print(f"Evento: {evento['nombre']}, Fecha: {evento['fecha']}, Hora: {evento['hora']}, Lugar: {evento['lugar']}")
    print()

def detalles_eventos():
    artista_id = input("Ingrese su ID de artista: ")
    asignaciones = u.leer_json("asignaciones_artistas.json")
    if asignaciones is None or len(asignaciones) == 0:
        print("No hay asignaciones de presentaciones.")
        return
    mis_asignaciones = [a for a in asignaciones if a['artista_id'] == artista_id]
    if len(mis_asignaciones) == 0:
        print("No tiene presentaciones asignadas.")
        return
    eventos = u.leer_json("eventos.json")
    if eventos is None:
        print("No hay eventos disponibles.")
        return
    print(">>>> Detalles de Eventos Asignados <<<<<")
    for asignacion in mis_asignaciones:
        evento = next((e for e in eventos if e['id'] == asignacion['evento_id']), None)
        if evento:
            print(f"ID: {evento['id']}, Nombre: {evento['nombre']}, Fecha: {evento['fecha']}, Hora: {evento['hora']}, Lugar: {evento['lugar']}, Capacidad: {evento['capacidad']}")
    print()

# ASISTENTES CRUD
def ver_eventos_disponibles():
    eventos = u.leer_json("eventos.json")
    if eventos is None or len(eventos) == 0:
        print("No hay eventos disponibles.")
        return
    print(">>>> Eventos Disponibles <<<<<")
    for evento in eventos:
        print(f"ID: {evento['id']}, Nombre: {evento['nombre']}, Fecha: {evento['fecha']}, Hora: {evento['hora']}, Lugar: {evento['lugar']}, Capacidad: {evento['capacidad']}")
    print()

def inscripcion_evento():
    ver_eventos_disponibles()
    evento_id = input("Ingrese el ID del evento al que desea inscribirse: ")
    asistente_id = input("Ingrese su ID de asistente: ")
    # Verificar si el evento existe
    eventos = u.leer_json("eventos.json")
    if eventos is None:
        print("No hay eventos disponibles.")
        return
    evento = next((e for e in eventos if e['id'] == evento_id), None)
    if evento is None:
        print("Evento no encontrado.")
        return
    # Verificar si ya está inscrito
    inscripciones = u.leer_json("inscripciones.json")
    if inscripciones is None:
        inscripciones = []
    if any(i['asistente_id'] == asistente_id and i['evento_id'] == evento_id for i in inscripciones):
        print("Ya está inscrito en este evento.")
        return
    # Registrar inscripción con estado "en espera"
    nueva_inscripcion = {
        "asistente_id": asistente_id,
        "evento_id": evento_id,
        "estado": "en espera"
    }
    inscripciones.append(nueva_inscripcion)
    u.escribir_json(inscripciones, "inscripciones.json")
    print("Inscripción realizada con éxito. Estado: en espera.")

def cancelar_inscripcion():
    asistente_id = input("Ingrese su ID de asistente: ")
    evento_id = input("Ingrese el ID del evento a cancelar: ")
    inscripciones = u.leer_json("inscripciones.json")
    if inscripciones is None:
        print("No hay inscripciones.")
        return
    inscripcion = next((i for i in inscripciones if i['asistente_id'] == asistente_id and i['evento_id'] == evento_id), None)
    if inscripcion is None:
        print("Inscripción no encontrada.")
        return
    if inscripcion['estado'] == "cancelado":
        print("La inscripción ya está cancelada.")
        return
    inscripcion['estado'] = "cancelado"
    u.escribir_json(inscripciones, "inscripciones.json")
    print("Inscripción cancelada con éxito.")

def boletos_incripciones():
    asistente_id = input("Ingrese su ID de asistente: ")
    inscripciones = u.leer_json("inscripciones.json")
    if inscripciones is None:
        print("No hay inscripciones.")
        return
    mis_inscripciones = [i for i in inscripciones if i['asistente_id'] == asistente_id]
    if len(mis_inscripciones) == 0:
        print("No tiene inscripciones.")
        return
    print(">>>> Mis Inscripciones <<<<<")
    for i in mis_inscripciones:
        print(f"Evento ID: {i['evento_id']}, Estado: {i['estado']}")
    print()

def actualizar_estado_inscripcion():
    asistente_id = input("Ingrese su ID de asistente: ")
    evento_id = input("Ingrese el ID del evento: ")
    nuevo_estado = input("Ingrese el nuevo estado (confirmado/cancelado): ").lower()
    if nuevo_estado not in ["confirmado", "cancelado"]:
        print("Estado inválido. Debe ser 'confirmado' o 'cancelado'.")
        return
    inscripciones = u.leer_json("inscripciones.json")
    if inscripciones is None:
        print("No hay inscripciones.")
        return
    inscripcion = next((i for i in inscripciones if i['asistente_id'] == asistente_id and i['evento_id'] == evento_id), None)
    if inscripcion is None:
        print("Inscripción no encontrada.")
        return
    if inscripcion['estado'] != "en espera":
        print("Solo se puede actualizar el estado si está en 'en espera'.")
        return
    inscripcion['estado'] = nuevo_estado
    u.escribir_json(inscripciones, "inscripciones.json")
    print(f"Estado actualizado a '{nuevo_estado}' con éxito.")
