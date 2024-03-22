import random, numpy as np

def inicio_entrenamiento(salidas, m_umbrales, m_pesos, patrones_X, patrones_Y, max_iteraciones, error_maximo_permitido):
    num_iteraciones = 0             # Numero de veces que ha iterado
    RA = 0.1                        # Rata de Aprendizaje
    error_iteracion = float('inf')  # Inicializamos el error de la iteracion a un valor infinito
    m_pesos_actual = m_pesos        # Se establece la matriz de peso 
    m_umbrales_actual = m_umbrales  # Se establece la matriz de umbrales 
    error_patrones = [0] * len(patrones_X)  # Lista para almacenar errores por patrón   

    while (error_iteracion > error_maximo_permitido) and (num_iteraciones < max_iteraciones):   # Iteraciones entrenamiento
        num_patron, fA= 0, 0
        while (num_patron < len(patrones_X)):   # Iteraciones por Patron 
            # Obtener el patron de la iteracion de X
            patron_actual_X = patrones_X[num_patron]
            # Funcion Soma, Salida Atenuada y Funcion de Activacion (Limitador Duro)
            fA = calculo_funciones(patron_actual_X, m_pesos_actual, m_umbrales_actual)
            # Calculo Error Lineal
            error_lineal, error_patrones[num_patron] = calculo_error_patron(patrones_Y, fA, num_patron, salidas)
            # Modificacion pesos y umbrales para el siguiente patron
            m_pesos_actual, m_umbrales_actual = calculo_pesos_umbrales(m_pesos_actual, m_umbrales_actual, RA, error_lineal, patron_actual_X) 
            # Pasa al siguiente patron
            num_patron += 1
        # Se calcula el error de iteracion
        error_iteracion 
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
    return fA

def calculo_error_patron(patrones_Y, fA, num_patron, salidas):
    patron_Y = np.array(patrones_Y[num_patron])
    fA = np.array(fA)
    # Error lineal
    error_lineal = patron_Y - fA
    # Error por patron
    error_patron = (np.sum(np.abs(error_lineal))/len(salidas))
    return error_lineal, error_patron

def calculo_pesos_umbrales (m_pesos, m_umbrales, RA,  error_lineal, patron_X):
    W = np.array(m_pesos)
    u = np.array(m_umbrales)
    X = np.array(patron_X)
    EL = np.array(error_lineal)
    m_peso_nuevo = (W + RA * EL[:, np.newaxis] * X).tolist()
    m_umbral_nuevo = (u + RA * 1).tolist()
    return m_peso_nuevo, m_umbral_nuevo