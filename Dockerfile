FROM python:3.9


# Set environment variables
ENV DB_USER=user
ENV DB_PASSWORD=app
ENV DB_SERVICE=student-db-service
ENV DB_NAME=student

# Set the working directory in the container
WORKDIR /app


RUN apt-get update -y 

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

ENV FLASK_APP=main.py


CMD ["gunicorn", "-b", "0.0.0.0:5000", "--timeout", "1500", "main:app"]