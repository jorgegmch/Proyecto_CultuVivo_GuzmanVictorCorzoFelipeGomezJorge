import utils as u

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
    artistas=u.leer_json("Artistas.json")
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
    u.escribir_json(artistas,"Artistas.json")
    

def monitorear_aforo():
    eventos=u.leer_json("eventos.json")
    for i, evento in enumerate(eventos, 1):
        print(f"Evento {i}: {evento['nombre']}")
    op_evento= input("Seleccione un evento:  ")
    
    
    


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
    pass

def detalles_eventos():
    pass

# ASISTENTES CRUD
def ver_eventos_disponibles():
    pass

def inscripcion_evento():
    pass

def cancelar_inscripcion():
    pass

def boletos_incripciones():
    pass