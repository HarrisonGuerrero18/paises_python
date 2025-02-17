#Crear la aplicación: Flask

#1) Importar Flask

from flask import Flask

#2) Crear la aplicación con esa dependencia:

app = Flask(__name__)

#Crear una ruta de prueba:
@app.route('/prueba') 
def prueba():
    return 'Hola, mundo!'