#Definir rutas de prueba

#1) Importar el modulo de la Aplicación centra(la carpeta app)

from app import app

#Crear una ruta de prueba:
@app.route('/prueba') 

def prueba():
    return 'Hola, mundo!'