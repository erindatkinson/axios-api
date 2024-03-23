#!/usr/bin/env python
"""the main module is the entrypoint for the api"""
from flask import Flask, request, jsonify, json
from flask_cors import CORS
import db


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = db.url
db.engine.init_app(app)


@app.get("/tasks")
def list_todos():
    """list_todos
        Desc: Handler for the /tasks GET route
        Produces: json"""
    all_tasks = db.session.query(db.Task).all()
    return jsonify(all_tasks), 200


@app.post("/tasks")
def new_todo():
    """new_todo
        Desc: Handler for the /tasks POST route
        Accepts: json
        Produces: json"""
    data = dict(json.loads(request.get_data()))
    try:
        todo_id = data["id"]
        name = data["name"]
        complete = data["completed"]
    except KeyError as ke:
        return f"bad data: {ke}", 400

    todo = db.Task(id=todo_id, name=name, completed=complete)
    db.session.add(todo)
    db.session.commit()

    return jsonify(todo), 201


@app.get("/tasks/<string:todo_id>")
def get_todo(todo_id: str):
    """get_todo
        Desc: Handler for the /tasks/:id GET route
        Produces: json"""
    todo = db.engine.get_or_404(db.Task, todo_id)
    return jsonify(todo), 200


@app.patch("/tasks/<string:todo_id>")
def update_todo(todo_id: str):
    """update_todo
        Desc: Handler for the /tasks/:id PATCH route
        Accepts: json
        Produces: json"""
    todo = db.engine.get_or_404(db.Task, todo_id)
    data = dict(json.loads(request.get_data()))
    updateable = False
    if "name" in data:
        todo.name = data["name"]
        updateable = True
    if "completed" in data:
        todo.completed = data["completed"]
        updateable = True

    if updateable:
        db.session.commit()

    return jsonify(todo), 200


@app.delete("/tasks/<string:todo_id>")
def delete_todo(todo_id: str):
    """delete_todo
        Desc: Handler for the /tasks/:id DELETE route"""
    todo = db.engine.get_or_404(db.Task, todo_id)
    db.session.delete(todo)
    db.session.commit()
    return "", 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
