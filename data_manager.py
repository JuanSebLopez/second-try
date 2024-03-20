import random

def procesar_datos(entradas, salidas):
    # Calcular cantidad de datos en las matrices de peso y umbrales. Patrones
    cant_peso = len(entradas) * len(salidas)
    cant_umbral = len(salidas)
    cant_patrones = len(list(entradas.values())[0])

    # Se llena la matriz de peso con valores aleatorios entre 0 y 1
    m_pesos = [round(random.randint(1, 9) / 10, 1) for _ in range(cant_peso)]
    # Se llena la matriz de umbrales con valores a  leatorios entre -1 y 1
    m_umbral = [round(random.randint(-10, 10) / 10, 1) for _ in range(cant_umbral)]

    # Pasar el diccionario de entradas y salidas a indices de valores normales
    entradas, salidas = obtener_entradas_salidas(entradas, salidas)

    # Obtener los Patrones
    patrones = obtener_patrones(cant_patrones)
    return patrones, cant_patrones, cant_umbral, cant_peso

def obtener_patrones(cant_patrones):
    patrones = []
    for i in range(cant_patrones):
        patron = []
        for entrada in entradas.values():
            patron.append(entrada[i])
        patrones.append(patron)
    return patrones

def obtener_entradas_salidas(dicc_entradas, dicc_salidas):
    entradas = []
    salidas = []
    for i in range(len(dicc_entradas)):
        entrada = []
        for entrada_data in entradas.values():
            entrada.append(entrada_data[i])
        entradas.append(entrada)

    for i in range(len(dicc_salidas)):
        salida = []
        for salida_data in salidas.values():
            salida.append(salida_data[i])
        salidas.append(salida)
    return entradas, salidas

def hola ():
    return "hola :D"