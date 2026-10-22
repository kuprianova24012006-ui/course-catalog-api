# Course Catalog API

A REST API for managing and retrieving course information, built with FastAPI and Pydantic.

## Features

- Retrieve all courses
- Retrieve a course by ID
- Filter courses by elective status
- Sort courses by popularity or title
- Paginate course results
- Interactive API documentation

## Technologies

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn

## Installation

1. Clone the repository.
2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the environment on Windows:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the API

```bash
fastapi dev main.py
```

The API will be available at http://127.0.0.1:8000.

## API Documentation

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/courses` | Retrieve all courses |
| GET | `/courses/{course_id}` | Retrieve a course by ID |

## Query Parameters

- `is_elective=true` or `false` — filter courses
- `sort=popular` — sort by likes, descending
- `sort=title` — sort alphabetically
- `skip` — number of courses to skip
- `limit` — maximum number of courses to return
