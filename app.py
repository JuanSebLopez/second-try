from flask import Flask, render_template, request
from upload_utils import procesar_archivo
from data_manager import procesar_datos

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
        error_iteracion, m_peso, m_umbral= procesar_datos(entradas, salidas)
        return render_template('result.html', entradas=entradas, salidas=salidas)
    
if __name__ == '__main__':
    app.run(debug=True)