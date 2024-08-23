
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
    (or)
   sudo docker-compose up
   ```

3. **Access the application:**

   - **Backend**: The backend Django API will be accessible at `http://localhost:8000`.
   - **Frontend**: The frontend application will be accessible at `http://localhost:3000`. The frontend is included in the Docker Compose setup and is fetched from the `frontend` Docker image.

## Notes

- If you need to explore or modify the frontend project, you can visit the repository here: [Frontend Repo](https://github.com/sumanpitla/frontend).
- The `docker-compose.yml` file is configured to pull the frontend image, ensuring that both the backend and frontend work together seamlessly.

## Troubleshooting

If you encounter any issues, ensure that Docker and Docker Compose are installed correctly and that no other services are running on ports `8000` or `3000`.

## Images
![homepage](https://github.com/user-attachments/assets/ad315e47-3501-4650-8013-115ded43e110)
![addcourse](https://github.com/user-attachments/assets/c72ef859-4f89-4a98-a0d6-0bf6f7d026db)
![allcourses](https://github.com/user-attachments/assets/ac611332-c22a-408f-85a3-28753a12303f)
![Addinst](https://github.com/user-attachments/assets/ad71e123-802a-4d33-8f8a-9ea91ae1a69f)
![courseinstance](https://github.com/user-attachments/assets/ba352a5a-67ad-4378-a24b-ce6c935047fb)
![ListOutinsctnces](https://github.com/user-attachments/assets/c16d271f-c215-408d-9c33-74ed5ce66cdc)

## Video


https://github.com/user-attachments/assets/3385d35b-32e2-47e5-ac42-bc5131b2d8d6


