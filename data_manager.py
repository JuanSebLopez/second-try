import random
from model_training import inicio_entrenamiento

def procesar_datos(entradas, salidas):
    m_umbral, m_pesos, patrones_X, patrones_Y = definir_parametros_entrada(entradas, salidas)
    # Pasar el diccionario de entradas y salidas a indices de valores normales
    entradas, salidas = establecer_entradas_salidas(entradas, salidas)

    # TODO: Se añade el num de iteraciones maximas manual. Revisar despues como se obtendra
    error_iteracion, m_peso_nuevo, m_umbral_nuevo = inicio_entrenamiento (salidas, m_umbral, m_pesos, patrones_X, patrones_Y, 100, 0.1)
    return error_iteracion, m_peso_nuevo, m_umbral_nuevo

def definir_parametros_entrada (entradas, salidas):
    # Calcular cantidad de datos en las matrices de peso y umbrales. Patrones
    tam_m_peso = len(entradas) * len(salidas)
    tam_m_umbral = len(salidas)
    cant_patrones = len(list(entradas.values())[0])

    # Se llena la matriz de peso con valores aleatorios entre 0 y 1
    m_pesos = [round(random.randint(1, 9) / 10, 1) for _ in range(tam_m_peso)]
    # Se llena la matriz de umbrales con valores a  leatorios entre -1 y 1
    m_umbral = [round(random.randint(-10, 10) / 10, 1) for _ in range(tam_m_umbral)]

    # Obtener los Patrones de X y Y
    patrones_X, patrones_Y = obtener_patrones(cant_patrones, entradas, salidas)
    return m_umbral, m_pesos, patrones_X, patrones_Y

def obtener_patrones(cant_patrones, entradas, salidas):
    patrones_X, patrones_Y = [], []
    for i in range(cant_patrones):
        patron_X, patron_Y = [], []
        for entrada in entradas.values():
            patron_X.append(entrada[i])
        patrones_X.append(patron_X)
        for salida in salidas.values():
            patron_Y.append(salida[i])
        patrones_Y.append(patron_Y)
    return patrones_X, patrones_Y

def establecer_entradas_salidas(dicc_entradas, dicc_salidas):
    entradas = list(dicc_entradas.values())
    salidas = list(dicc_salidas.values())
    return entradas, salidas

def hola ():
    return "hola :D"