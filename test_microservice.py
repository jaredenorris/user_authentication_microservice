import requests

base_url = 'http://127.0.0.1:5001'  

# Register a new user
register_url = f'{base_url}/register'
register_data = {
    'username': 'test_user',
    'email': 'test@example.com',
    'password': 'test_password'
}
register_response = requests.post(register_url, json=register_data)
print('Register Response:', register_response.json())

# Login with the registered user
login_url = f'{base_url}/login'
login_data = {
    'username': 'test_user',
    'password': 'test_password'
}
login_response = requests.post(login_url, json=login_data)
print('Login Response:', login_response.json())

# Verify the token obtained from login
verify_url = f'{base_url}/verify'
verify_data = {
    'token': login_response.json().get('token')
}
verify_response = requests.post(verify_url, json=verify_data)
print('Verify Response:', verify_response.json())
