# DecodeLabs Project 2 — Backend API

A simple REST API developed using Python and Flask as part of the DecodeLabs Full Stack Development Internship.

This project focuses on developing backend API endpoints, handling HTTP requests and responses, validating input data, and returning JSON responses.

## Technologies Used

- Python
- Flask
- Flask-CORS
- REST API
- JSON
- HTML
- JavaScript

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/api/projects` | Get all projects |
| GET | `/api/projects/<id>` | Get a specific project |
| POST | `/api/projects` | Add a new project |

## POST Request

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
    "id": 6,
    "name": "Spam Detection System",
    "technology": "Python, NLP"
}
```

## Features

- REST API development using Flask
- JSON request and response handling
- GET and POST endpoints
- Dynamic project data
- Input validation
- CORS support
- Frontend API testing using HTML and JavaScript

## Project Structure

```text
Project2/
├── app.py
├── test.html
├── requirements.txt
└── README.md
```

## What I Learned

- Building REST APIs using Flask
- Understanding HTTP methods
- Creating API endpoints
- Handling JSON data
- Validating incoming requests
- Returning JSON responses
- Using Flask-CORS for frontend-backend communication
- Testing APIs from a frontend

## Author

**Manasa N S**

Computer Science Engineering Student

Interested in Backend Development and Software Engineering.