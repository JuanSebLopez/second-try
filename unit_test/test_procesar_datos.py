# Variable que almacena el diccionario de datos
entradas = {'e1': [0, 1, 1, 0, 0, 0, 0, 0, 1, 1], 'e2': [0, 1, 1, 0, 1, 1, 0, 0, 0, 0], 'e3': [0, 1, 1, 0, 1, 1, 1, 1, 1, 1], 'e4': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}
patrones_Y = []

# Lista para almacenar los patrones
patrones = []

# Obtener el número de elementos en cada entrada
num_elementos = len(list(entradas.values())[0])
print(f"Numero de elementos en entradas: {num_elementos}")

# Iterar sobre cada índice
for i in range(num_elementos):
    # Crear un patrón vacío para este índice
    patron = []
    
    # Iterar sobre cada entrada y obtener el valor en el índice actual
    for entrada in entradas.values():
        patron.append(entrada[i])
    
    # Agregar el patrón generado a la lista de patrones
    patrones.append(patron)

# Imprimir los patrones resultantes
print("Patrones:")
for idx, patron in enumerate(patrones):
    print(f"indice {idx} de patrones: {patron}")

