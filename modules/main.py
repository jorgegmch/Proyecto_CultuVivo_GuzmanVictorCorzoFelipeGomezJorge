from modules.utils import clear_screen, pause
from modules.messages import menu_login, menu_asistentes
from modules.CRUD import ver_eventos_disponibles, inscripcion_evento, boletos_incripciones, actualizar_estado_inscripcion, cancelar_inscripcion

def main_login():
    main_asistentes()

def main_asistentes():
    while True:
        menu_asistentes()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ver_eventos_disponibles()
            pause()
        elif opcion == "2":
            inscripcion_evento()
            pause()
        elif opcion == "3":
            boletos_incripciones()
            pause()
        elif opcion == "4":
            actualizar_estado_inscripcion()
            pause()
        elif opcion == "5":
            cancelar_inscripcion()
            pause()
        elif opcion == "6":
            print("Cerrando sesión.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            pause()

def main_artistas():
    pass

def main_admin():
    pass

def main_reportes():
    pass