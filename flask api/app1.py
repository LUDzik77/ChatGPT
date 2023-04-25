#run with venv venv1 activated
#if run via bash (export+run)--> http://localhost:5000 instead of 127.0.0.1:6969 
#it turns the run function and ignored the if __name__ etc

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return("hello world")

@app.route('/<_name>')
def print_name(_name):
    if app.debug == True:
        return(f'Hello {_name}, we run app in debug mode')
    return(f'Hello {_name}')

if __name__ == "__main__":
    app.run(port=6969, debug=True)