# DecodeLabs Project 2 - Backend API

A simple REST API developed using Python and Flask as part of the DecodeLabs Full Stack Development Internship.

## Technologies Used

- Python
- Flask
- Flask-CORS
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