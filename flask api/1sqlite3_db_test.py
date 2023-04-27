import sqlite3
import random

db =  sqlite3.connect("db_test.db")
cursor = db.cursor()

#cursor.execute("""
#CREATE TABLE scores(
#id integer,
#name string,
#surname string,
#score integer)
#""")


#cursor.execute("""INSERT into SCORES(id, name, surname, score) 
#VALUES (1, "Ludwik", "Papaj", 100)""")

names = ["Jan", "Tomasz", "Piotr"]
surnames = ["Nowak", "Kowalski", "Adamski"]
#random.choice(names), random.choice(surnames), random.randint(0,100)

#for nr in range(2,5):
    #_name    = random.choice(names)
    #_surname = random.choice(surnames)
    #_score  = random.randint(0,100)
    #values = (nr, _name, _surname, _score)
    #print(_name, _surname, _score)
    #cursor.execute(f" insert into scores values (?,?,?,?)", values)
    #db.commit()


cursor.execute("""SELECT * from scores """)
rows = cursor.fetchall()
for r in rows:
    print(r[1], r[2], r[3])
cursor.execute("""SELECT count(*) from scores """)
rows = cursor.fetchone()
print("Rows", rows[0])

db.commit()
db.close()