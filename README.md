
# Backend Project: Course Management System

This repository contains the backend of the Course Management System, developed using Django REST API. The Docker and Docker Compose files are located in the `backend/course_management` directory. This setup allows you to run the backend as a Docker container, and it also integrates the frontend via Docker Compose. If you want to explore the frontend project, please visit the following repository: [Frontend Repo](https://github.com/sumanpitla/frontend).

## Prerequisites

Ensure that you have the following installed on your local machine:

- **`Operating System`**:(Ubuntu(Recommended),Linux,windows)
- Docker
- Docker Compose

## Project Structure

- **`backend/course_management/`**: Contains the Django REST API application and the necessary Docker and Compose files.

## Docker Setup

The backend project is containerized using Docker. The Docker image for the frontend project is also included in the `docker-compose.yml` file to run both the backend and frontend simultaneously.

## Running the Project

To run the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sumanpitla/backend.git
   cd backend/course_management
   ```

2. **Run the Docker Compose:**

   The `docker-compose.yml` file will pull the necessary images for both the backend and frontend, and it will start the services.

   ```bash
   docker-compose up
   ```

3. **Access the application:**

   - **Backend**: The backend Django API will be accessible at `http://localhost:8000`.
   - **Frontend**: The frontend application will be accessible at `http://localhost:3000`. The frontend is included in the Docker Compose setup and is fetched from the `frontend` Docker image.

## Notes

- If you need to explore or modify the frontend project, you can visit the repository here: [Frontend Repo](https://github.com/sumanpitla/frontend).
- The `docker-compose.yml` file is configured to pull the frontend image, ensuring that both the backend and frontend work together seamlessly.

## Troubleshooting

If you encounter any issues, ensure that Docker and Docker Compose are installed correctly and that no other services are running on ports `8000` or `3000`.
