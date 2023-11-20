# User Authentication Microservice README

## Communication Contract

### Introduction

This README outlines the communication contract for interacting with the microservice implemented in this repository. The microservice creates and stores user profile data, and it communicates with the main app via http requests.

### Requesting Data
```
import requests

# Example: Requesting data from the microservice to verify a token
url = "http://localhost:5001/verify"
token = "your_jwt_token_here"  

data = {"token": token}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Token is valid")
else:
    print(f"Token verification failed. Response: {response.json()}")
```
Replace "your_jwt_token_here" with an actual JWT token that you want to verify. This script sends a POST request to the /verify endpoint of your microservice, providing the token in the request body. The microservice responds with a message indicating whether the token is valid.

### Receiving Data

```
import requests

# Example: Requesting data from the microservice to register a new user
url = "http://localhost:5001/register"

user_data = {
    "username": "new_user",
    "email": "new_user@example.com",
    "password": "new_password"
}

response = requests.post(url, json=user_data)

# Assuming the microservice returns JSON responses
if response.status_code == 201:
    print("User registration successful!")
    print(response.json())
else:
    print(f"User registration failed. Response: {response.json()}")
```
The script sends a POST request to the /register endpoint of your microservice, providing user registration data in the request body. The microservice responds with a message indicating whether the user registration was successful, along with any additional information.

### Example Response
User registration successful!
User registration failed. Response:

### UML Sequence Diagram

![Microservice Diagram](microservice/microservice_diagram.png)

