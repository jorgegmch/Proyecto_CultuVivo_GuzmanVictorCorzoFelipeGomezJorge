import os
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione ENTER para continuar...")

def validador_capacidadmaxima():
    pass

def validador_fecha():
    pass

def validador_hora():
    pass

def asignar_boleto():
    pass

def validador_imput():
    pass

def escribir_json(datos, archivo):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"Datos escritos exitosamente en {archivo}")
    except Exception as e:
        print(f"Error al escribir en {archivo}: {e}")

def leer_json(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        return datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON en {archivo}.")
        return None
    except Exception as e:
        print(f"Error al leer {archivo}: {e}")
        return None
