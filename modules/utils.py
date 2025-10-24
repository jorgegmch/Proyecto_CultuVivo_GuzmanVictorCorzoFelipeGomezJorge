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

def escribir_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def leer_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)