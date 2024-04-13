# Use an official Python runtime as a parent image
# FROM python:3.9
FROM --platform=linux/amd64 python:3.9

# Set environment variables
ENV XDG_RUNTIME_DIR=/tmp/runtime-root

# Set environment variables
ENV DB_USER=user
ENV DB_PASSWORD=app
ENV DB_SERVICE=student-db-service
ENV DB_NAME=student

# Set the working directory in the container
WORKDIR /app

# Install wkhtmltopdf
RUN apt-get update -y 

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

ENV FLASK_APP=main.py

# Make port 5000 available to the world outside this container
# EXPOSE 5000

# Run gunicorn when the container launches
# CMD ["gunicorn", "-b", "0.0.0.0:8070", "--timeout", "530", "main:app"]

# CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "--timeout", "1500", "main:app"]