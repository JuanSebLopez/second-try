import numpy as np

def calculo_funciones (patron_actual_X, m_pesos_actual, m_umbrales_actual):
    X = np.array(patron_actual_X)
    W = np.array(m_pesos_actual)
    u = np.array(m_umbrales_actual)
    
    # Verifica las dimensiones de X y W
    if X.ndim == 1:  # Si X es un vector (1D)
        X = X.reshape(-1, 1)  # Conviértelo en una matriz columna
    if W.ndim == 1:  # Si W es un vector (1D)
        W = W.reshape(-1, 1)  # Conviértelo en una matriz columna
    
    # Calcula la función Soma
    S = np.dot(X, W)
    
    # Calcula S_Atenuada
    S_atenuada = S - u
    
    # Calcula la Funcion de Activacion (Limitador Duro)
    e_salida = np.where(S_atenuada >= 0, 1, 0)
    fA = e_salida.tolist()
    
    return fA

def calculo_pesos_umbrales (m_pesos, m_umbrales, RA,  error_lineal, patron_X):
    W = np.array(m_pesos)
    u = np.array(m_umbrales)
    X = np.array(patron_X)
    EL = np.array(error_lineal)

    EL = EL.reshape(-1, 1)  # Convierte EL en una matriz columna
    X = X.reshape(1, -1)  # Convierte X en una matriz fila

    # Realiza la actualización de los pesos y umbrales
    m_peso_nuevo = (W + RA * np.dot(EL, X))  # Utiliza np.dot para la multiplicación de matrices
    m_umbral_nuevo = (u + RA * 1)

    m_peso_nuevo = m_peso_nuevo.squeeze()
    return m_peso_nuevo, m_umbral_nuevo