# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /backend/course_management

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run migrations
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


# FROM python:3.10
# RUN apt update && apt install -y git
# RUN git clone https://github.com/sumanpitla/backend.git
# WORKDIR /backend/course_management
# RUN pip install -r requirements.txt
# RUN python manage.py migrate
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver"]