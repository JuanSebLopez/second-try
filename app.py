from flask import Flask, render_template, request
from upload_utils import procesar_archivo
from data_manager import procesar_datos
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']

    entradas, salidas, error = procesar_archivo(file)
    print(entradas, salidas)

    if error:
        return error
    else:
        error_iteracion, m_peso, m_umbral, salidas_reales, salidas_esperadas= procesar_datos(entradas, salidas)
        # Grafica Error de Iteración vs Número de Iteración
        plt.plot(error_iteracion)
        plt.xlabel('Numero de Iteracion')
        plt.ylabel('Error de Iteracion')
        plt.title('Error de Iteracion vs Numero de Iteracion')
        img_data = io.BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        img_base64 = base64.b64encode(img_data.getvalue()).decode()
        plt.close()

        return render_template('result.html', entradas=entradas, salidas=salidas, error_iteracion_img=img_base64, salidas_esperadas=salidas_esperadas, salidas_reales=salidas_reales)
    
if __name__ == '__main__':
    app.run(debug=True)