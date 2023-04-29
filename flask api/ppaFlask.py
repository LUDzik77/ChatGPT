from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("glowna.html")

@app.route("/czesc")
@app.route("/czesc/<imie>")
def czesc(imie=None):
    return render_template("czesc.html", imie=imie)

@app.route("/hej/<imie>")
def powitanie(imie):
    return (f"Czesc, {imie}")
    
@app.route("/users/<int:id>")
def info_user(id):
    return(f"Dane użytkownika o id {id}")
           
if __name__ == "__main__":
    app.run(port=6969)
    