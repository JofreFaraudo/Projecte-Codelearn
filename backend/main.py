from flask import Flask
from flask import request
app = Flask(__name__)
import sqlite3
conn = sqlite3.connect("todos.db")
c = conn.cursor()
@app.route("/todo", methods=["GET"])
def llistar():
    a = c.execute('''SELECT * FROM todos''')
    result = []
    for i in a:
       result.append({'id':i[0],'name':i[1],'state':i[2]})
    return "{ 'todos':"+str(result)+"}"

@app.route("/todo", methods=["DELETE"])
def delete():
    id_todo = request.get_json()['id']
    try:
        a = c.execute('''SELECT id FROM todos WHERE id=:id''', {"id":id_todo})
        if len(a.fetchall()) == 0:
            return "{'status':'err'}"
    except sqlite3.Error as error:
        return "{'status':'err'}"
    try:
        c.execute('''DELETE FROM todos WHERE id=:id''', {"id":id_todo})
    except sqlite3.Error as error:
        return "{'status':'err'}"
    return "{'status' : 'ok'}"

@app.route("/todo", methods=["POST"])
def new():
    nom = request.get_json()['name']
    c.execute('''INSERT INTO todos (desc, fet) VALUES ("'''+nom+'''" , 0)''')
    id_de_todo = c.execute('''SELECT id FROM todos WHERE desc=:nom''', {"nom": nom}) 
    id_todo = id_de_todo.fetchone()[0]
    return "{'id' : "+str(id_todo)+"}"

@app.route("/todo", methods=["PUT"])
def update():
    id_todo = request.get_json()['id']
    try:
        a = c.execute('''SELECT id FROM todos WHERE id=:id''', {"id":id_todo})
        if len(a.fetchall()) == 0:
            return "{'status':'err'}"
    except sqlite3.Error as error:
        return "{'status':'err'}"
    if "name" in list(request.get_json().keys()):
        nom = request.get_json()['name']
        try:
            c.execute('''UPDATE todos SET desc="'''+str(nom)+'''" WHERE id='''+str(id_todo))
        except sqlite3.Error as eror:
            return "{'status':'err'}"
    if "state" in list(request.get_json().keys()):
        estat = request.get_json()['state']
        try:
            c.execute('''UPDATE todos SET fet='''+str(estat)+''' WHERE id='''+str(id_todo))
        except sqlite3.Error as eror:
            return "{'status':'err'}"
    return "{'status' : 'ok'}"

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port=5000)
