import random, numpy as np

def inicio_entrenamiento(salidas, m_umbrales, m_pesos, patrones_X, patrones_Y, max_iteraciones, error_maximo_permitido):
    # Se establece el num_iteraciones y la rata de aprendizaje para empezar el entrenamiento. 
    num_iteraciones = 0
    rata_aprendizaje = round(random.randint(1,9) / 10, 1)
    error_iteracion = float('inf')  # Inicializamos el error de la iteracion a un valor infinito
    m_pesos_actual = m_pesos        # Se establece la matriz de peso y umbrales actuales y anteriores 
    m_umbrales_actual = m_umbrales

    while (error_iteracion > error_maximo_permitido) and (num_iteraciones < max_iteraciones):
        num_patron, S, S_atenuada, fA = 0, 0, 0, 0  
        m_pesos_ant, m_umbrales_ant, error_patrones = [], [], []
        # Empezar iteraciones
        while (num_patron < len(patrones_X)):
            # Obtener el patron de la iteracion de X y Y
            patron_actual_X = patrones_X[num_patron]
            patron_actual_Y = patrones_Y[num_patron]
            # Funcion Soma, Salida Atenuada y Funcion de Activacion (Limitador Duro)
            S, S_atenuada, fA = calculo_funciones(patron_actual_X, m_pesos_actual, m_umbrales_actual)
            # Calculo Error Lineal
            error_lineal, error_patrones[num_patron] = calculo_errores(patrones_Y, fA, num_patron, salidas)
            # Modificacion pesos y umbrales para el siguiente patron
            
            # Pasa al siguiente patron
            num_patron += 1
        num_iteraciones += 1
    return None

def calculo_funciones (patron_actual_X, m_pesos_actual, m_umbrales_actual):
    X = np.array(patron_actual_X)
    W = np.array(m_pesos_actual)
    u = np.array(m_umbrales_actual)
    # Calculo funcion Soma
    S = np.dot(X, W)
    # Calculo S_Atenuada
    S_atenuada = S - u
    #Calculo Funcion de Activacion (Limitador Duro)
    e_salida = np.where(S_atenuada >= 0, 1, 0)
    fA = e_salida.tolist()
    return S, S_atenuada, fA

def calculo_errores(patrones_Y, fA, num_patron, salidas):
    patron_Y = np.array(patrones_Y[num_patron])
    fA = np.array(fA)
    # Error lineal
    error_lineal = patron_Y - fA
    # Error por patron
    error_patron = (np.sum(error_lineal)/len(salidas))
    return error_lineal, error_patron