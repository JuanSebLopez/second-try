import json
import xml.etree.ElementTree as ET
import graphviz

def procesar_archivo(file):
    if file.filename.endswith('.json'):
        try:
            data = json.load(file)
            # Verifica si se encuentran las claves 'entrada' y 'salida'
            if 'entradas' in data and 'salidas' in data:
                entradas = data['entradas']
                salidas = data['salidas']
                return entradas, salidas, None
            else:
                return None, None, 'Error: El archivo JSON no contiene las claves necesarias'
        except json.JSONDecodeError:
            return None, None, 'Error: El archivo JSON está mal formateado'
    else:
        return None, None, 'Error: El archivo debe tener extensión .json'
    
def combinar_data(entradas, salidas):
    data = []

    for key, value in entradas.items():
        data.append({'Nombre':key, 'Valores': value})
    for key, value in salidas.items():
        data.append({'Nombre':key, 'Valores': value})
    return data

#def visualizar_neurona(inputs, weights, threshold):
#    dot = graphviz.Digraph()
#    dot.node('Neurona', 'Neurona', shape='circle')
#    for i, input_val in enumerate(inputs):
#        dot.node(f'Entrada_{i}', f'Entrada_{i+1}', shape='oval')
#        dot.edge(f'Entrada_{i}', 'Neurona', label=str(weights[i]))
#    dot.node('Umbrales', f'Umbrales', shape='diamond')
#    dot.edge('Umbrales', 'Neurona', label=str(threshold))
#    dot.render('static/neurona', format='png', cleanup=True)  # Guarda la imagen en la carpeta 'static'
#    return 'neurona.png'  # Devuelve el nombre del archivo