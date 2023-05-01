from flask import Flask, render_template, request
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

engine = create_engine('sqlite:///testDB_ppaFlask.db')
with engine.connect() as conn:
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testDB_ppaFlask.db"

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    
#@app.route("/")
#def hello():
#    return render_template("glowna.html")

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
#tasks = ["shopping", "cleaning"]
 
@app.route("/", methods =["GET", "POST"])
def todo():
    #tasks = ["shopping", "cleaning"]
    if request.method == "POST":
        task = Task(name=request.form["task"])
        db.session.add(task)
        db.session.commit()
    tasks =Task.query.all()
        #tasks.append(request.form['tasks'])
    return render_template("todo.html", tasks=tasks)

if __name__ == "__main__":
    app.run(port=6969)
    
    #db.create_all()
    #task1 = Task(name = "shopping_new")
    #task2 = Task(name = "cleaning_new")
    #db.session.add(task1)
    #db.session.add(task2)
    #db.session.commit()
    #Task.query.all()
