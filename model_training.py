import random, numpy as np

def inicio_entrenamiento(m_umbrales, m_pesos, m_patrones, max_iteraciones, error_maximo_permitido):
    # Se establece el num_iteraciones y la rata de aprendizaje para empezar el entrenamiento. 
    num_iteraciones = 0
    rata_aprendizaje = round(random.randint(1,9) / 10, 1)
    error_iteracion = float('inf')  # Inicializamos el error de la iteracion a un valor infinito
    m_pesos_actual = m_pesos        # Se establece la matriz de peso y umbrales actuales y anteriores 
    m_umbrales_actual = m_umbrales

    while (error_iteracion > error_maximo_permitido) and (num_iteraciones < max_iteraciones):
        num_patron, S, S_atenuada, fA = 0
        m_pesos_ant, m_umbrales_ant = []
        # Empezar iteraciones
        while (num_patron < len(m_patrones)):
            # Obtener el patron de la iteracion
            patron_actual = m_patrones[num_patron]
            # Obtener matrices de Umbrales y Pesos
            
            # Funcion Soma, Salida Atenuada y Funcion de Activacion (Limitador Duro)
            S, S_atenuada, fA = calculo_funciones(patron_actual, m_pesos_actual, m_umbrales_actual)
            # Calculo Error Lineal

            
            # Pasa al siguiente patron
            num_patron += 1
        num_iteraciones += 1
    return None

def calculo_funciones (patron_actual, m_pesos_actual, m_umbrales_actual):
    X = np.array(patron_actual)
    W = np.array(m_pesos_actual)
    u = np.array(m_umbrales_actual)
    # Calculo funcion Soma
    S = np.dot(X, W)
    # Calculo S_Atenuada
    S_atenuada = S - u
    #Calculo Funcion de Activacion (Limitador Duro)
    fA = np.where(S_atenuada >= 0, 1, 0)

    return S, S_atenuada, fA

def error_lineal():
    1