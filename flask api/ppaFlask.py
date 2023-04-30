from flask import Flask, render_template, request

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

#we can  move it to sqllite db later on
tasks = ["shopping", "cleaning"]
 
@app.route("/todo", methods =["GET", "POST"])
def todo():
    #tasks = ["shopping", "cleaning"]
    if request.method == "POST":
        tasks.append(request.form['tasks'])
    return render_template("todo.html", tasks=tasks)

if __name__ == "__main__":
    app.run(port=6969)
    
