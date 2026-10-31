from pathlib import Path
import sqlite3

from flask import Flask, abort, redirect, render_template, request, url_for


app = Flask(__name__)
DATABASE = Path(__file__).with_name("tasks.db")


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                is_done INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


@app.get("/")
def index():
    with get_connection() as connection:
        tasks = connection.execute(
            "SELECT id, title, is_done FROM tasks ORDER BY is_done, id DESC"
        ).fetchall()
    return render_template("index.html", tasks=tasks)


@app.post("/tasks")
def add_task():
    title = request.form.get("title", "").strip()
    if title:
        with get_connection() as connection:
            connection.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/toggle")
def toggle_task(task_id):
    with get_connection() as connection:
        result = connection.execute(
            "UPDATE tasks SET is_done = CASE is_done WHEN 0 THEN 1 ELSE 0 END WHERE id = ?",
            (task_id,),
        )
        if result.rowcount == 0:
            abort(404)
    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/delete")
def delete_task(task_id):
    with get_connection() as connection:
        result = connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if result.rowcount == 0:
            abort(404)
    return redirect(url_for("index"))


initialize_database()


if __name__ == "__main__":
    app.run(debug=True)
