from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'thisisasecretkey'

# create a connection to the database
def get_db():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

# create the table if it doesn't exist
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks';")
        table_exists = cursor.fetchone()
        if not table_exists:
            with app.open_resource('schema.sql', mode='r') as f:
                cursor.executescript(f.read())
            db.commit()

# home page
@app.route('/')
def index():
    db = get_db()
    tasks = db.execute('SELECT * FROM tasks ORDER BY id DESC').fetchall()
    return render_template('index.html', tasks=tasks)

# add a task
@app.route('/add', methods=['POST'])
def add():
    db = get_db()
    db.execute('INSERT INTO tasks (task) VALUES (?)', [request.form['task']])
    db.commit()
    return redirect(url_for('index'))

# delete a task
@app.route('/delete/<int:id>')
def delete(id):
    db = get_db()
    db.execute('DELETE FROM tasks WHERE id = ?', [id])
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    #init_db()
    app.run()