# Lunch Voting App

Lunch Voting App is a FastAPI-based application for organizing voting on lunch dishes. The system allows users to register, view restaurants and their menus, and vote for their favorite dishes. The application uses PostgreSQL for data storage, Alembic for managing database migrations, and Docker for creating an isolated and reproducible environment.

## Table of Contents
1. [Getting Started](#getting-started)
2. [How to Run the Application](#how-to-run-the-application)
3. [Environment Variables](#environment-variables)
4. [Testing](#testing)
5. [Project Structure and Design Decisions](#project-structure-and-design-decisions)

---

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed and running.
- **Python (optional)**: Required only for local development outside of Docker.

Clone the repository and navigate to the project directory:

```bash
  git clone https://github.com/OleksiukStepan/lunch-voting-app
  cd lunch-voting-app
```
---

## How to Run the Application

1. **Start with Docker Compose**:
    ```bash
    docker-compose up --build
    ```

   This command will:
    - Create a PostgreSQL container for data storage.
    - Automatically apply all necessary Alembic migrations at container startup.
    - Start the FastAPI server at http://0.0.0.0:8000.

2. **API Documentation**:

   Open your browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to view the interactive API documentation.

---

## Environment Variables

The project uses environment variables to configure the database and other settings.
A sample file named `.env.sample` is provided in the project root. Follow these steps to set up your environment:


1. **Copy the Sample File**  
   Create a new file named `.env` by copying the sample:
   ```bash
   cp .env.sample .env
   ```
   
2. **Fill in the Required Values**
   Open the .env file in your text editor and provide the necessary values. For example:


    POSTGRES_DB=lunch
    POSTGRES_DB_PORT=5432
    POSTGRES_USER=stepan
    POSTGRES_PASSWORD=stepan_password
    POSTGRES_HOST=db

    DATABASE_URL=postgresql://stepan:stepan_password@db:5432/lunch

    SECRET_KEY=your_secure_secret_key_here


  - POSTGRES_DB: The name of your PostgreSQL database (e.g., lunch).
  - POSTGRES_DB_PORT: The port on which PostgreSQL is running (default is 5432).
  - POSTGRES_USER: The username for the PostgreSQL database (e.g., stepan).
  - POSTGRES_PASSWORD: The password for the PostgreSQL user (e.g., stepan_password).
  - POSTGRES_HOST: The hostname for PostgreSQL. Use db when running in Docker; for local development, you may set this to localhost.
  - DATABASE_URL: The full connection string matching the above settings.
  - SECRET_KEY: A secure secret key for your application.


3. **Usage in Docker and Alembic**

Docker Compose: The docker-compose.yml file loads these variables from the .env file automatically.
Alembic: In alembic/env.py, the DATABASE_URL is read from the environment and overrides the default value in alembic.ini, ensuring that migrations use the correct connection string.

---

## Testing

To run tests for the application, ensure that the containers are running, then execute the following command:

```bash
   docker exec -it backend_fastapi pytest /usr/fastapi/backend/tests
```

---

## Project Structure and Design Decisions

- **Models**:  
  The project includes the following core models:
    - **User** – represents a user who can vote.
    - **Restaurant** – represents a restaurant providing menus.
    - **Menu** – represents a restaurant’s menu which users can vote on.
    - **Vote** – records a user's vote for a specific menu item.

- **Database and Migrations**:  
  PostgreSQL is used for data storage, and Alembic manages schema versioning.

- **Docker**:  
  The project is fully containerized using Docker and Docker Compose, providing an isolated development and deployment environment.

- **FastAPI**:  
  FastAPI is used to build a high-performance API with interactive Swagger documentation.
