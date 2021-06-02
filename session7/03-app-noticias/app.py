from flask import Flask
import json
from flask import render_template
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def index():
    token = request.args.get("token")
    f = open("data/news.json", "r")
    data = json.load(f)
    ispremium = token != None
    return render_template('lista.html', news = data, ispremium = ispremium)