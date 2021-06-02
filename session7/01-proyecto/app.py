from flask import Flask
from flask.helpers import send_file, send_from_directory

app = Flask(__name__)

@app.route('/robot.txt')
def robots():
    return send_file('robots.txt')

@app.route('/assets/<path:filename>') #http://localhost:5000/assets/frutas/Fresa.jpg
def assets(filename):
    return send_from_directory('assets', filename)

# La ruta puede ser cualquiera, en la parte ultima
#Tengo que decirle en q carpeta buscar, y q archivo
@app.route('/assets/<name>.css') #/styles.css
def css(name):
    return send_from_directory('assets', f'{name}.css')