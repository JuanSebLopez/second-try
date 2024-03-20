import random

def inicio_entrenamiento(umbrales, pesos, patrones):
    # Se establece el num_iteraciones y la rata de aprendizaje para empezar el entrenamiento. 
    num_iteraciones = 0
    rata_aprendizaje = round(random.randint(1,9) / 10, 1)
    error_iteracion = float('inf') # Inicializamos el error de la iteracion a un valor infinito
    error_maximo_permitido = 0.1 # Se establece el error maximo permitido para el entrenamiento de la red.

    while (error_iteracion > error_maximo_permitido):
        1