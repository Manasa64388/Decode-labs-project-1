# DecodeLabs Project 3 — Database Integration & CRUD API

A Flask REST API integrated with SQLite for persistent project data, developed as part of the DecodeLabs Full Stack Development Internship.

This project extends backend API development by introducing database integration and complete CRUD operations for managing project records.

## Technologies Used

- Python
- Flask
- SQLite
- Flask-CORS
- REST API
- JSON
- SQL

## Database

The application uses SQLite to store project information persistently.

The `projects` table contains:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Unique project identifier |
| `name` | TEXT | Project name |
| `technology` | TEXT | Technology used in the project |

The project table is automatically created when the application starts if it does not already exist.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/api/projects` | Retrieve all projects |
| POST | `/api/projects` | Create a new project |
| PUT | `/api/projects/<id>` | Update an existing project |
| DELETE | `/api/projects/<id>` | Delete a project |

## CRUD Operations

### Create — POST

Endpoint:

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

Example response:

```json
{
    "message": "Project created successfully",
    "id": 1,
    "name": "Spam Detection System",
    "technology": "Python, NLP"
}
```

### Read — GET

Endpoint:

```text
GET /api/projects
```

Returns all projects stored in the SQLite database.

### Update — PUT

Endpoint:

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

The API verifies that the requested project exists before updating it.

### Delete — DELETE

Endpoint:

```text
DELETE /api/projects/<id>
```

The API verifies that the requested project exists before deleting it.

## Validation & Error Handling

The API includes validation and error handling for:

- Missing request body
- Missing `name` or `technology`
- Project not found
- Invalid project IDs

Example error response:

```json
{
    "error": "Project not found"
}
```

## Features

- Flask REST API
- SQLite database integration
- Complete CRUD operations
- Persistent project storage
- Automatic database table creation
- JSON request and response handling
- Input validation
- 404 error handling
- CORS support
- Parameterized SQL queries

## Project Structure

```text
Project3/
├── app.py
├── database.db
├── test.html
├── requirements.txt
└── README.md
```

## What I Learned

- Integrating SQLite with Flask
- Creating and managing database tables
- Performing SQL queries from Python
- Implementing CRUD operations
- Using parameterized SQL queries
- Handling database records through REST APIs
- Validating API requests
- Handling missing database records
- Building persistent backend applications

## Author

**Manasa N S**

Computer Science Engineering Student

Interested in Backend Development and Software Engineering.