from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

projects = [
    {
    "id" : 1,
    "name" : "Smart Fraud Detection System",
    "technology" : "Python, Machine LEarning"
},
{
    "id" : 2,
    "name" : "Water Demand Prediction",
    "technology" : "Python, Flask, Machine Learning"
},
{
    "id" : 3,
    "name" : "Hospital Readmission Prediction",
    "technology" : "Python, Machine Learning"
}
]
@app.route("/")
def home():
    return {
        "message": "DecodeLabs Project 2 API is running"
    }

@app.route("/api/projects", methods=["GET"])
def get_projects():
    return projects

@app.route("/api/projects", methods=["POST"])
def add_projects():
    data = request.get_json()

    if not data:
        return {"error" : "Request body is required"}, 400

    if "name" not in data or "technology" not in data:
        return {
            "error" : "name and technology are required"
        }, 400
    new_project = {
        "id" : len(projects) + 1,
        "name" : data["name"],
        "technology" : data["technology"]
    }
    projects.append(new_project)
    return new_project, 201

@app.route("/api/projects/<int:project_id>", methods=["GET"])
def get_project(project_id):
    for project in projects:
        if project["id"] == project_id:
            return project, 200

    return {
        "error": "Project not found"
    }, 404

if __name__ == "__main__":
    app.run(debug=True)
    