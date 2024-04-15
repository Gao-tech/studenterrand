# The application
The application is to maanage students complaints. The collected data will be
queried and used to analyze and improve the students working environment.
Students can login, signup, logout. They need to choose faculty, program 
and which semester that they're studying.In the end recordcomplaint. Then the
responsible people will cope with the errands. They need to report the process 
and mostly specify on which management level that they solve it.


# Python Flask, Bootstrap, MySQL, Docker and Azure Web App service

Use paython flask framework to complete login, sign up, sign off etc.functions.
It also controls input of email, errand and password
and connect bootstrap to build frontend.
The app uses MySQL as a database.
create a docker file that contains Python and database information
Deploy into Azure cloud

## Installation

Database installation: All the python environment and libraries, MySQL, 
Docker desktop.

```bash
pip install all the requirements
```

## Azure deployment docker file
This is my azure docker compose file for deployment
```docker
version: "3.9"
services:
  db-service:
    container_name: "db-service"
    image: mysql
    environment:
      - MYSQL_ROOT_PASSWORD=root
      - MYSQL_DATABASE=student-db
      - MYSQL_USER=new-user
      - MYSQL_PASSWORD=appleW00d
    volumes:
      - "db_data:/var/lib/mysql"
   

  student-service:
    container_name: "student-service"
    image: gaojiejessi/studenterrand:13
    restart: always
    environment:
      - DB_USER=new-user
      - DB_PASSWORD=appleW00d
      - DB_SERVICE=db-service
      - DB_NAME=student-db        

    depends_on:
      - db-service
    ports:
      - "80:5000"
   
volumes:
    db_data:
```

## Contributing

The app runs fine on my computer with Python and MySQL.
I made a docker file of Python and database together.

         1. It works fine with commands on terminal:

                docker compose up --build
         2. I then use the commands to tag docker image.

               docker build -t gaojiejessi/student .

         3.I send image "gaojiejessi/student" to Docker Hub.

         4. Extract image for Azure Web App Deployment

         5. Deploy the app from Azure Web App Deployment center. 



