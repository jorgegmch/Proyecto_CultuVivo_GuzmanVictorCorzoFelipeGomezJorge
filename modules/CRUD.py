import modules.utils as u
from datetime import datetime

#login
def login():
    try:
        usuarios = u.leer_json("Usuarios.json")
    except FileNotFoundError:
        usuarios = {}
    usuario = input("   Login: ")
    print("\nUsuario no existe!!❌   \n\nIntente nuevamente o precione '0' para salir.\n ")
    for k, v in usuarios.items():
        for login in v["login"]:
            if login == usuario:
                return k


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
    u.escribir_json("eventos.json",eventos)

def registro_artistas():
    artistas=u.leer_json("artistas.json")
    if artistas is None:
        artistas = []
    print(">>>>> Nuevo Artista <<<<<\n")
    id_artista=input("> ID : ")
    nombre=input("> Nombre: ")
    tipo_presentacion=input("> Tipo de presentación: ")
    tiempo_presentacion=input("> Tiempo de Presentación: ")
    
    nuevo_artista= {
        "id_artista" : id_artista,
        "nombre": nombre,
        "tipo_presentacion":tipo_presentacion,
        "tiempo": tiempo_presentacion        
    }
    artistas.append(nuevo_artista)
    u.escribir_json("artistas.json",artistas)


def monitorear_aforo():
    eventos=u.leer_json("eventos.json")
    for i, evento in enumerate(eventos, 1):
        print(f"Evento {i}: {evento['nombre']}")
    op_evento= input("Seleccione un evento:  ")
    

# ADMINS REPORTES
def participacion_artistas():
    artistas = u.leer_json("artistas.json")
    asignaciones = u.leer_json("asignaciones_artistas.json")
    if artistas is None or asignaciones is None:
        print("No hay datos disponibles.")
        return
    participacion = {}
    for artista in artistas:
        id_artista = artista['id_artista']
        count = sum(1 for a in asignaciones if a['artista_id'] == id_artista)
        participacion[id_artista] = {'nombre': artista['nombre'], 'eventos': count}
    print(">>>> Participación de Artistas <<<<<")
    for id_artista, data in participacion.items():
        print(f"ID: {id_artista}, Nombre: {data['nombre']}, Eventos: {data['eventos']}")
    print()

def ver_proximos_eventos():
    eventos = u.leer_json("eventos.json")
    if eventos is None:
        print("No hay eventos disponibles.")
        return
    hoy = datetime.now().date()
    proximos = []
    for evento in eventos:
        try:
            fecha_evento = datetime.strptime(evento['fecha'], '%Y-%m-%d').date()
            if fecha_evento >= hoy:
                proximos.append(evento)
        except ValueError:
            continue  # Skip invalid dates
    proximos.sort(key=lambda x: x['fecha'])
    print(">>>> Próximos Eventos <<<<<")
    for evento in proximos:
        print(f"ID: {evento['id']}, Nombre: {evento['nombre']}, Fecha: {evento['fecha']}, Hora: {evento['hora']}, Lugar: {evento['lugar']}")
    print()

def listado_asistentes():
    asistentes = u.leer_json("Asistentes.json")
    if asistentes is None or len(asistentes) == 0:
        print("No hay asistentes registrados.")
        return
    print(">>>> Listado de Asistentes <<<<<")
    for asistente in asistentes:
        print(f"Nombre: {asistente['nombre']}, Cédula: {asistente['cedula']}, Correo: {asistente['correo']}, Estado: {asistente['estado']}, Tipo Boleta: {asistente['tipo_boleta']}")
    print()

def eventos_menos_asistentes():
    eventos = u.leer_json("eventos.json")
    inscripciones = u.leer_json("inscripciones.json")
    if eventos is None or inscripciones is None:
        print("No hay datos disponibles.")
        return
    conteo = {}
    for evento in eventos:
        id_evento = evento['id']
        count = sum(1 for i in inscripciones if i['evento_id'] == id_evento and i['estado'] == 'confirmado')
        conteo[id_evento] = {'nombre': evento['nombre'], 'asistentes': count}
    if not conteo:
        print("No hay eventos con asistentes confirmados.")
        return
    min_asistentes = min(conteo.values(), key=lambda x: x['asistentes'])['asistentes']
    eventos_menos = [data for data in conteo.values() if data['asistentes'] == min_asistentes]
    print(">>>> Eventos con Menos Asistentes Confirmados <<<<<")
    for evento in eventos_menos:
        print(f"Nombre: {evento['nombre']}, Asistentes Confirmados: {evento['asistentes']}")
    print()

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
    print(">>>> Agenda de Presentaciones <<<<<\n")
    for asignacion in mis_asignaciones:
        evento = next((e for e in eventos if e['id'] == asignacion['evento_id']), None)
        if evento:
            print(f"Evento: {evento['nombre']} \nFecha: {evento['fecha']} \nHora: {evento['hora']} \nLugar: {evento['lugar']}\n")
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
def nuevo_asistente():
    nombre = input("Nombre Completo: ")
    id = input("Cedula: ")
    correo = input("Correo: ")
    
    # Leer asistentes existentes o iniciar lista vacía
    try:
        total_asistentes = u.leer_json("Asistentes.json")
    except FileNotFoundError:
        total_asistentes = []

    # Verificar si el asistente ya existe
    for asistente in total_asistentes:
        if asistente["cedula"] == id:
            print("Ese asistente ya existe")
            return

    # Agregar nuevo asistente
    total_asistentes.append({
        "nombre": nombre,
        "cedula": id,
        "correo": correo,
        "estado":"",
        "tipo_boleta": ""
    })
    
    # Leer usuarios existentes o iniciar dict por defecto
    try:
        asistentes = u.leer_json("Usuarios.json")
    except FileNotFoundError:
        asistentes = {"asistente": {"login": []}}
    
    # Agregar ID al login si no existe
    if id not in asistentes["asistente"]["login"]:
        asistentes["asistente"]["login"].append(id)
    
    # Escribir de vuelta
    u.escribir_json("Asistentes.json", total_asistentes)
    u.escribir_json("Usuarios.json", asistentes)
    print(f"{nombre} Registrado correctamete! ")

def ver_eventos_disponibles():
    eventos = u.leer_json("eventos.json")
    if eventos is None or len(eventos) == 0:
        print("No hay eventos disponibles.")
        return
    print(">>>> Eventos Disponibles <<<<<")
    for evento in eventos:
        print(f"N°:{evento['id']}\n Nombre: {evento['nombre']}\n Fecha: {evento['fecha']}\n Hora: {evento['hora']}\n Lugar: {evento['lugar']}\n")
    print()


def inscripcion_evento():
    ver_eventos_disponibles()
    evento_id = input("Ingrese el N° del evento al que desea inscribirse: ")
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
    u.escribir_json("inscripciones.json", inscripciones)    
    print("Inscripción realizada con éxito. Estado: en espera.")

def cancelar_inscripcion():
    asistente_id = input("Ingrese su ID de asistente: ")
    evento_id = input("Ingrese el N° del evento a cancelar: ")
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
    u.escribir_json("inscripciones.json", inscripciones)
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
    print("\n>>>> Mis Inscripciones <<<<<\n")
    for i in mis_inscripciones:
        print(f"Evento N°: {i['evento_id']}, Estado: {i['estado']}")
    print()

def actualizar_estado_inscripcion():
    asistente_id = input("Ingrese su ID de asistente: ")
    evento_id = input("Ingrese el N° del evento: ")
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
    u.escribir_json("inscripciones.json", inscripciones)
    print(f"Estado actualizado a '{nuevo_estado}' con éxito.")
