#run with venv venv1 activated
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return("hello world")