from flask import Flask
from flask.templating import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    noticias = ["Debate del domingo 23 de mayo",
    "¿Cómo saber si tengo multas electorales",
    "El revelador informe que el Pentágono alista sobre EEUU"
    ]
    name = request.args.get("name")
    return render_template("index.html", title="Home", name = name, noticias = noticias)

