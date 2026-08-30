# DecodeLabs Project 4 — Full-Stack Project Manager

A full-stack project management application developed as part of the DecodeLabs Full Stack Development Internship.

This project integrates a Flask backend, SQLite database, REST API, and JavaScript frontend into a single application for managing project records.

## Technologies Used

### Backend

- Python
- Flask
- Flask-CORS
- SQLite
- REST API
- JSON

### Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API

## Architecture

The application follows a simple full-stack architecture:

```text
Frontend
   │
   │ HTTP Requests
   ▼
Flask REST API
   │
   │ SQL Queries
   ▼
SQLite Database
```

The frontend communicates with the Flask backend using the JavaScript Fetch API. The backend processes the requests and stores or retrieves project data from the SQLite database.

## Features

- Add new projects
- View all projects
- Edit existing projects
- Delete projects
- Persistent project storage using SQLite
- REST API integration
- JSON request and response handling
- Input validation
- Error handling
- CORS support
- Responsive frontend interface
- Confirmation before deleting a project

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/api/projects` | Retrieve all projects |
| POST | `/api/projects` | Add a new project |
| PUT | `/api/projects/<id>` | Update an existing project |
| DELETE | `/api/projects/<id>` | Delete a project |

## CRUD Operations

### Create — POST

```text
POST /api/projects
```

Example request:

```json
{
    "name": "Spam Detection System",
    "technology": "Python, NLP"
}
```

### Read — GET

```text
GET /api/projects
```

Returns all projects stored in the SQLite database.

### Update — PUT

```text
PUT /api/projects/<id>
```

Example request:

```json
{
    "name": "Updated Project",
    "technology": "Python, Flask"
}
```

### Delete — DELETE

```text
DELETE /api/projects/<id>
```

The application asks for confirmation before deleting a project from the frontend.

## Frontend

The frontend provides a simple project management interface.

Users can:

- Enter a project name
- Enter the technology used
- Add a project
- View saved projects
- Edit project details
- Delete projects

The frontend uses the JavaScript Fetch API to communicate with the Flask REST API asynchronously.

## Database

SQLite is used for persistent storage.

The `projects` table contains:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Unique project identifier |
| `name` | TEXT | Project name |
| `technology` | TEXT | Technology used |

The database table is automatically created when the application starts if it does not already exist.

## Validation & Error Handling

The backend validates incoming requests before modifying the database.

It handles:

- Missing request body
- Missing project name
- Missing technology
- Project not found
- Invalid requests

Example error response:

```json
{
    "error": "Project not found"
}
```

## Project Structure

```text
Project4/
├── app.py
├── database.db
├── requirements.txt
├── README.md
└── frontend/
    ├── index.html
    ├── script.js
    └── style.css
```

## How to Run

### 1. Navigate to Project4

```bash
cd Project4
```

### 2. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask server

```bash
python app.py
```

The backend runs at:

```text
http://127.0.0.1:5000
```

### 5. Open the frontend

Open:

```text
frontend/index.html
```

in a web browser.

Make sure the Flask server is running while using the frontend because the frontend communicates with the backend API.

## What I Learned

- Integrating a frontend with a Flask backend
- Building REST APIs using Flask
- Connecting Flask applications with SQLite
- Implementing complete CRUD operations
- Using the JavaScript Fetch API
- Sending and receiving JSON data
- Handling asynchronous API requests
- Validating user input
- Handling API errors
- Using CORS for frontend-backend communication
- Building a simple full-stack application

## Author

**Manasa N S**

Computer Science Engineering Student

Interested in Backend Development and Software Engineering.