from flask import Flask, request
from flask_cors import CORS
import sqlite3
app = Flask(__name__)
CORS(app)
DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        technology TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return {
        "message": "Project 3 API is running"
    }


@app.route("/api/projects", methods=['POST'])
def create_project():
    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    name = data.get("name")
    technology = data.get("technology")

    if not name or not technology:
        return {"error": "name and technology are required"}, 400

    conn = get_db_connection()

    cursor = conn.execute(
        "INSERT INTO projects (name, technology) VALUES (?, ?)",
        (name, technology)
    )

    conn.commit()

    project_id = cursor.lastrowid

    conn.close()

    return {
        "message": "Project created successfully",
        "id": project_id,
        "name": name,
        "technology": technology
    }, 201 

@app.route("/api/projects", methods=["GET"])
def get_projects():
    conn = get_db_connection()

    projects = conn.execute(
        "SELECT * FROM projects"
    ).fetchall()

    conn.close()

    return [dict(project) for project in projects]

@app.route("/api/projects/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    name = data.get("name")
    technology = data.get("technology")

    if not name or not technology:
        return {"error": "name and technology are required"}, 400

    conn = get_db_connection()

    project = conn.execute(
        "SELECT * FROM projects WHERE id = ?",
        (project_id,)
    ).fetchone()

    if project is None:
        conn.close()
        return {"error": "Project not found"}, 404

    conn.execute(
        """
        UPDATE projects
        SET name = ?, technology = ?
        WHERE id = ?
        """,
        (name, technology, project_id)
    )

    conn.commit()
    conn.close()

    return {
        "message": "Project updated successfully",
        "id": project_id,
        "name": name,
        "technology": technology
    }

@app.route("/api/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    conn = get_db_connection()

    project = conn.execute(
        "SELECT * FROM projects WHERE id = ?",
        (project_id,)
    ).fetchone()

    if project is None:
        conn.close()
        return {"error": "Project not found"}, 404

    conn.execute(
        "DELETE FROM projects WHERE id = ?",
        (project_id,)
    )

    conn.commit()
    conn.close()

    return {
        "message": "Project deleted successfully",
        "id": project_id
    }

init_db()

if __name__ == "__main__":
    app.run(debug=True)
