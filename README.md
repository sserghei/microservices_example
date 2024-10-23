This project consists of three microservices:
1. **Public Gateway** (Node.js): Exposed to the public and proxies requests to private services.
2. **Auth Service** (Ruby): Handles authentication.
3. **User Service** (Python): Manages user information.

## Prerequisites
- Docker
- Docker Compose

## Setup

1. Clone the repositories:
    - Clone the repository for each service.
    - Make sure you have the correct structure:
        ```
        project/
        ├── auth_service/
        ├── user_service/
        ├── public_gateway/
        └── docker-compose.yml
        ```

2. Build and run the services:

    Run the following command to start all services:
    ```bash
    docker-compose up --build
    ```

## Access the services

- **Public Gateway**: Exposed on `http://localhost:8080`.
  - Example to authenticate:
    ```
    curl "http://localhost:8080/auth/1"
    ```
  - Example to retrieve user information:
    ```
    curl "http://localhost:8080/user/2"
    ```

The `public_gateway` will forward requests to the appropriate private services (`auth_service` and `user_service`).

### Network

- All private services are accessible only via Docker's internal network, and they communicate through HTTP.