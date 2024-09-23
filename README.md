# JWT Authentication API for Odoo

This module implements JWT (JSON Web Token) authentication for Odoo, providing secure login and protected API access using token-based authentication. The module includes endpoints for login, token refresh, and protected resources, ensuring that users can authenticate and access data securely via RESTful APIs.

## Features
- **JWT-based Authentication**: Users can log in and receive a JWT token that can be used to authenticate subsequent API requests.
- **Token Refresh**: An endpoint to refresh the JWT token before it expires.
- **Protected Routes**: API routes are protected using a JWT token, ensuring only authenticated users can access these resources.
- **Custom Odoo Integration**: Utilizes Odoo's session authentication mechanism combined with JWT tokens for seamless integration with Odoo's user model.

## Endpoints
The following endpoints are exposed:

### `/api/auth/login`
- **Method**: POST
- **Description**: This endpoint authenticates the user and returns a JWT token if the credentials are valid.
- **Parameters**:
  - `email`: The user's email (Odoo login).
  - `password`: The user's password.
- **Response**: 
  - Success: 
    ```json
    {
      "token": "<JWT_TOKEN>"
    }
    ```
  - Error (invalid credentials):
    ```json
    {
      "error": "Invalid credentials"
    }
    ```

### `/api/auth/refresh`
- **Method**: POST
- **Description**: Refreshes an existing JWT token before it expires.
- **Parameters**:
  - `token`: The JWT token to be refreshed.
- **Response**: 
  - Success:
    ```json
    {
      "token": "<NEW_JWT_TOKEN>"
    }
    ```
  - Error (invalid or expired token):
    ```json
    {
      "error": "Token has expired" 
    }
    ```

### `/api/protected`
- **Method**: GET
- **Description**: This endpoint returns a protected resource, requiring the user to be authenticated with a valid JWT token.
- **Headers**:
  - `Authorization`: `Bearer <JWT_TOKEN>`
- **Response**: 
  - Success:
    ```json
    {
      "message": "Welcome <user_name>, this is a protected resource!"
    }
    ```
  - Error (missing or invalid token):
    ```json
    {
      "error": "Missing or invalid token"
    }
    ```

## Installation

1. Clone the repository into your Odoo custom addons folder:
   ```bash
   install it like any odoo module 
   no need to tell you :D
