from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)
import sqlite3
conn = sqlite3.connect("todos.db")
c = conn.cursor()

error_status = {'status': 'err'}
ok_status = {'status': 'ok'}

# Select todos according to a filter
def select_todos(filter = {}):
    base_query = '''SELECT * FROM todos'''

    if len(filter) != 0:
        base_query += " WHERE "
        first = True
        for key in filter:
            if first:
                base_query += str(key) + "=" + str(filter[key])  
                first = False
            else:
                base_query += " AND " + str(key) + "=" + str(filter[key])

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

def updateStateTodo(state, id):
    try:
        a = c.execute('''UPDATE todos SET fet=:state WHERE id=:id''', {"state": state, "id": id})
    except sqlite3.Error as error:
        print("SQLite Error:", error.message)
        return False
    else:
        return True

def updateNameTodo(name, id):
    try:
        a = c.execute('''UPDATE todos SET desc="'''+name+'''" WHERE id=:id''', {"id":id})
    except sqlite3.Error as error:
        print("SQLite Error:", error.message)
        return False
    else:
        return True
@app.route("/todo", methods=["GET"])
def llistar():
    a = select_todos()
    if not a:
        return jsonify({"result": False})

    result = []
    for i in a:
       result.append({'id':i[0],'name':i[1],'state':i[2]})
    res = {}
    res["todos"] = result
    return jsonify(res)

@app.route("/todo", methods=["DELETE"])
def delete():
    id_todo = request.get_json()['id']

    todo = select_todos({"id": id_todo})
    if not todo:
        return jsonify(error_status)
    if not deleteTodo(id_todo):
        return jsonify(error_status)

    return jsonify(ok_status)

@app.route("/todo", methods=["POST"])
def new():
    nom = request.get_json()['name']
    c.execute('''INSERT INTO todos (desc, fet) VALUES ("'''+nom+'''" , 0)''')
    id_de_todo = c.execute('''SELECT MAX(id) FROM todos WHERE desc=:nom''', {"nom": nom}) 
    id_todo = id_de_todo.fetchone()[0]
    return jsonify("{'id' : "+str(id_todo)+"}")

@app.route("/todo", methods=["PUT"])
def update():
    id_todo = dict(request.get_json())['id']

    todo = select_todos({"id": id_todo})
    if not todo:
        return jsonify(error_status)

    if "name" in request.get_json():
        if not updateNameTodo(request.get_json()['name'],id_todo):
            return jsonify(error_status)
    if "state" in request.get_json():
        print(request.get_json())
        if not updateStateTodo(request.get_json()['state'],id_todo):
            print("s'ha retornat false");
            return jsonify(error_status)
    return jsonify(ok_status)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
