from flask import Flask, render_template, request
from upload_utils import procesar_archivo

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
        return render_template('result.html', entradas=entradas, salidas=salidas)
    #Entradas [e1, e2, e3, e... e_n]
    #Salidas [s1, s2, s3, s... s_n]
if __name__ == '__main__':
    app.run(debug=True)