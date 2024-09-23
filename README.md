# JWT Authentication API for Odoo

This module implements JWT (JSON Web Token) authentication for Odoo, providing secure login and protected API access
using token-based authentication. The module includes endpoints for login, token refresh, and protected resources,
ensuring that users can authenticate and access data securely via RESTful APIs.

## Features

- **JWT-based Authentication**: Users can log in and receive a JWT token that can be used to authenticate subsequent API
  requests.
- **Token Refresh**: An endpoint to refresh the JWT token before it expires.
- **Protected Routes**: API routes are protected using a JWT token, ensuring only authenticated users can access these
  resources.
- **Custom Odoo Integration**: Utilizes Odoo's session authentication mechanism combined with JWT tokens for seamless
  integration with Odoo's user model.

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
- **Description**: This endpoint returns a protected resource, requiring the user to be authenticated with a valid JWT
  token.
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

## How It Works

- **Authentication Flow**

The user sends their login credentials (email and password) to the /api/auth/login endpoint.
If the credentials are valid, the system generates a JWT token using the user's ID (sub) and email, which is then
returned to the client.

The token has a default expiration of 1 hour.
The client needs to store this token and send it in the Authorization
header for future requests to protected resources.

Token Refresh Flow
Before the JWT token expires, the client can call the /api/auth/refresh endpoint with the existing token.

The system will issue a new token with an extended expiration time (another 1 hour) and return it to the client.

If the token has already expired, the client must log in again.

- **JWT Token Protection**

Routes that need protection are decorated with the @jwt_required decorator. This decorator extracts the token from the
Authorization header and verifies it.

If the token is valid, the associated user is attached to the request object, allowing the route to access the user's
information.

If the token is missing, invalid, or expired, the route will return a 401 Unauthorized or 403 Forbidden error.
Token Generation and Verification
Tokens are generated using the HS256 algorithm with a secret key stored in the module (SECRET_KEY).

The token payload contains the user's ID (sub), email, and expiration time (exp).

During the request, the token is verified by decoding it with the same secret key, and the user's information is
extracted.

- **Code Structure**

controllers/jwt_auth_controller.py: Contains the main logic for handling JWT login, token refresh, and the protected
resource.

utils/jwt_auth.py: A utility file for token generation and verification, as well as the JWT decorator used to protect
routes.

controllers/controllers.py
login Function: Authenticates the user, generates a JWT token, and returns it to the client.

refresh_token Function: Refreshes an existing JWT token before it expires and returns a new one.

protected_resource Function: A protected endpoint that can only be accessed by authenticated users.

utils/jwt_auth.py
generate_token Function: Generates a new JWT token given a user ID and email, with an expiration time of 1 hour.

jwt_required Decorator: Verifies the JWT token in the request's Authorization header and ensures the user is
authenticated.

- **PostMan**

file postman.json ready to use 
