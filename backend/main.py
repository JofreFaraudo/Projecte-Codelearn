from flask import Flask
from flask import request
app = Flask(__name__)
import sqlite3
conn = sqlite3.connect("todos.db")
c = conn.cursor()

error_status = "{'status': 'err'}"
ok_status = "{'status': 'ok'}"

# Select todos according to a filter
def select_todos(filter = {}):
    base_query = '''SELECT * FROM todos'''

    if len(filter) != 0:
        base_query += " WHERE "
        first = True
        for key in filter:
            if first:
                base_query += key + "=" + filter[key]  
                first = False
            else:
                base_query += " AND " + key + "=" + str(filter[key])

    todos = c.execute(base_query)
    todos = todos.fetchall()

    if len(todos) == 0:
        return False
    return todos

def deleteTodo(id):
    try:
        a = c.execute('''DELETE FROM todos WHERE id=:id''', {"id":id})
    except sqlite3.Error as error:
        print("SQLite Error:", error.message)
        return False

@app.route("/todo", methods=["GET"])
def llistar():
    a = select_todos()
    result = []
    for i in a:
       result.append({'id':i[0],'name':i[1],'state':i[2]})
    return "{ 'todos':"+str(result)+"}"

@app.route("/todo", methods=["DELETE"])
def delete():
    id_todo = request.get_json()['id']

    todo = select_todos({"id": id_todo})
    if not todo:
        return error_status

    if not deleteTodo(id_todo):
        return error_status

    return ok_status

@app.route("/todo", methods=["POST"])
def new():
    nom = request.get_json()['name']
    c.execute('''INSERT INTO todos (desc, fet) VALUES ("'''+nom+'''" , 0)''')
    id_de_todo = c.execute('''SELECT MAX(id) FROM todos WHERE desc=:nom''', {"nom": nom}) 
    id_todo = id_de_todo.fetchone()[0]
    return "{'id' : "+str(id_todo)+"}"

@app.route("/todo", methods=["PUT"])
def update():
    id_todo = request.get_json()['id']

    todo = select_todos({"id": id_todo})
    if not todo:
        return error_status

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
