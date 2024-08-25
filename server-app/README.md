# Server-App (FastAPI Backend) - Python

## Overview

This project is a backend service built using FastAPI. It provides API endpoints for managing and retrieving balance sheet data. The structure of the project is designed to be modular, scalable, and easy to maintain.

## Project Structure

```bash
    ├── Dockerfile
    ├── README.md
    ├── app
    │   ├── main.py
    │   ├── config
    │   │   └── balance_types.py
    │   ├── routers
    │   │   └── balance_sheet.py
    │   └── services
    │       └── balance_sheet.py
    ├── requirements.txt
    └── tests
        ├── test_auth.py
        └── test_endpoint.py
```

## Key Directories and Files:

- `Dockerfile`: Used for containerizing the application.
- `README.md`: This file, providing an overview and documentation for the project.
- `app`: Main application directory.
  - `config`: Contains configuration files and types related to the balance sheet.
  - `routers`: Houses the route definitions for the FastAPI application.
  - `services`: Contains the business logic, interacting with databases or other external services.
  - `main.py`: Entry point for the FastAPI application.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `tests`: Directory for test cases.
  - `test_auth.py`: Tests related to authentication.
  - `test_endpoint.py`: Tests related to the API endpoints.

## Setup and Installation

### Prerequisites

- Python 3.8+
- Docker (optional but recommended for containerization)

### Installation

1. Clone the repository:

   ```bash
   $ https://github.com/Bina-man/code-drills.git
   $ cd code-drills
   $ git fetch origin
   $ git checkout -b production origin/production
   $ git checkout production
   $ cd server-app
   ```

2. Create and activate a virtual environment
    ```bash
   $ python3 -m venv venv
   ```

3. Install the dependencies
    ```bash
   $ pip3 install -r requirement.txt
   ```

## Running the Application

### Local Development
To run the FastAPI application locally:
```bash
$ uvicorn app.main:app --reload
```

### Docker setup
To run the FastAPI application locally:
```bash
$ docker build -t server-app .
$ docker run -d -p 8000:8000 server-app
```

## Testing

```bash
$ pytest
```