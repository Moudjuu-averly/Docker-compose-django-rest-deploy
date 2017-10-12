# Docker-compose-django-rest-deploy
Deploying a django based rest api with postgresql backend using docker-compose

###### 1. Create an empty project directory.
###### 2. Create a new file called Dockerfile in your project directory.
###### 3. Add the following content to the Dockerfile.
```
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
 
```
This Dockerfile starts with a Python 3 parent image. The parent image is modified by adding a new code directory.  
The parent image is further modified by installing the Python requirements defined in the requirements.txt file.  

###### 4. Save and close the Dockerfile.  
###### 5. Create a requirements.txt in your project directory.  

This file is used by the RUN pip install -r requirements.txt command in your Dockerfile.  

###### 6. Add the required software in the file.  

###### 7. Save and close the requirements.txt file.  

###### 8. Create a file called docker-compose.yml in your project directory.

The docker-compose.yml file describes the services that make your app. In this example those services   
are a web server and database. The compose file also describes which Docker images these services use,   
how they link together, any volumes they might need mounted inside the containers. Finally, the   
docker-compose.yml file describes which ports these services expose. See the docker-compose.yml   
reference for more information on how this file works.  

###### 9. Add the following configuration to the file.  

```
version: '3'

services:
  db:
    image: postgres
  web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```

This file defines two services: The db service and the web service.  

###### 10. Save and close the docker-compose.yml file.  



