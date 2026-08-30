# DecodeLabs Project 3 – Database Integration API

## Overview

A REST API built using **Python, Flask, and SQLite** as part of the DecodeLabs Full Stack Development Internship (Week 3).

This project demonstrates backend integration with a database and performs complete CRUD operations.

## Technologies Used

* Python
* Flask
* Flask-CORS
* SQLite3
* HTML
* JavaScript

## Database Schema

### Table: `projects`

| Column     | Type    | Description                  |
| ---------- | ------- | ---------------------------- |
| id         | INTEGER | Primary Key (Auto Increment) |
| name       | TEXT    | Project Name                 |
| technology | TEXT    | Technologies Used            |

## API Endpoints

| Method | Endpoint             | Description      |
| ------ | -------------------- | ---------------- |
| GET    | `/`                  | API Status       |
| GET    | `/api/projects`      | Get all projects |
| POST   | `/api/projects`      | Create project   |
| PUT    | `/api/projects/<id>` | Update project   |
| DELETE | `/api/projects/<id>` | Delete project   |

## Validation

* Returns **400** if required fields are missing.
* Returns **404** if a project ID does not exist.

## Run Locally

```bash
python -m venv .venv
```

Activate environment.

```bash
pip install -r requirements.txt
```

Run the server.

```bash
python app.py
```

Server URL:

```text
http://127.0.0.1:5000
```
