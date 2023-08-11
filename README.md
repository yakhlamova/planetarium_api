# Planetarium API Service

Welcome to the Planetarium API project! This API is designed to manage astronomy shows, show sessions, planetarium domes, and user reservations for a planetarium facility.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [API Documentation](#api-documentation)
- [DB Structure](#db-structure)
- [Contributing](#contributing)

## Features

- Manage astronomy shows and their details.
- Schedule and manage show sessions in different planetarium domes.
- Allow users to make reservations for show sessions.
- User authentication and authorization.
- Throttle API requests to prevent abuse.
- Add images for astronomy shows.

## Technologies Used
* Django
* Django REST framework
* Docker
* JWT Authentication
* Swagger/OpenAPI Documentation


## Getting Started

### Prerequisites
* Python (version 3.6 or higher) and pip installed on your system
* Git (optional, for cloning the repository)


### Installation
To set up the Planetarium API project using Docker, follow these steps:
1. Install Docker:
If you don't have Docker installed, you can download and install it from the official Docker website: https://docs.docker.com/get-docker/

2. Clone the repository:

   ```bash
   git clone https://github.com/yakhlamov/planetarium_api.git
   cd planetarium-api
   ```

3. Build the Docker Image:
    ```bash
   docker build -t planetarium-api .
    ```
 
4. Build the Docker containers using Docker Compose:
    ```bash
    docker-compose build
    ```

5. Create a superuser for accessing the Django admin panel and API:
    ```bash 
    docker exec -it <container_id here> python manage.py createsuperuser`
    ```    
   
6. Start the Docker containers:
    ``` bash 
    docker-compose up
   ```
## API Endpoints
```
"planetarium":
    "show_themes": "http://127.0.0.1:8000/api/planetarium/show_themes/",
    "astronomy_shows": "http://127.0.0.1:8000/api/planetarium/astronomy_shows/",
    "planetarium_domes": "http://127.0.0.1:8000/api/planetarium/planetarium_domes/",
    "show_sessions": "http://127.0.0.1:8000/api/planetarium/show_sessions/",
    "reservations": "http://127.0.0.1:8000/api/planetarium/reservations/"

"user":
    "registration": "http://127.0.0.1:8000/api/user/register/"
	"token": "http://127.0.0.1:8000/api/user/token/"
	
"documentatoin": 
	"http://127.0.0.1:8000/api/schema/" 
	"http://127.0.0.1:8000/api/schema/swagger/" 
	"http://127.0.0.1:8000/api/schema/redoc/"
```

## API Documentation
The API documentation can be accessed at http://localhost:8000/swagger/ which provides an interactive interface to explore and test the available API endpoints.

## DB Structure


## Contributing
I welcome contributions to improve the Planetarium API Service. Feel free to submit bug reports, feature requests, or pull requests to `yanaakhlamova@gmail.com`
