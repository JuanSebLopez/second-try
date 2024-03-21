import numpy as np

pesos = [[0.5,0.5], [0.5, 0], [-0.3, 0.3]]
patron_actual = [1,1,1]
# Definir las entradas X y los pesos W
X = np.array(patron_actual)  # Vector de entrada con 3 elementos
W = np.array(pesos)  # Matriz de pesos (3x2) para 3 entradas y 2 salidas

# Calcular la salida de la función soma
S = np.dot(X, W)

# Mostrar la salida
print("Salida de la funcion soma:", S)

# Definir la salida atenuada
S_atenuada = np.array([1.7, 2.8])

# Aplicar la función de activación (limitador duro)
YR = np.where(S_atenuada >= 0, 1, 0)

print("Salida atenuada:", S_atenuada)
print("Salida de la función de activación (limitador duro):", YR)

def calcular_error_lineal(Yd, YR):
    # Calcular el error lineal para cada patrón
    error_lineal = Yd - YR
    
    return error_lineal

# Ejemplo de uso
patrones_Y = [[0,0],[0,1],[1,0],[1,1]]
num_patron = 2
Yd = np.array(patrones_Y[num_patron])  # Salidas deseadas
y_r = [1,1]
YR = np.array(y_r) # Salidas calculadas por la red neuronal

# Calcular el error lineal
error_lineal = calcular_error_lineal(Yd, YR)

print("Error lineal:", error_lineal)
