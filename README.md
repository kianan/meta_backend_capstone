# Meta Backend Developer Professional Certificate Capstone Project

This is the capstone project for the Meta Backend Developer Professional Certificate. The project consists of a few API endpoints to manage restaurant bookings and menu items.


## Installation

- git clone https://github.com/kianan/meta_backend_capstone.git
- cd littlelemon
- pipenv shell
- pipenv install

My Sql Configuration

    1. Open littlelemon/settings.py.
	2. Locate the DATABASES section.
	3. Update the MySQL connection settings with your database credentials


``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your-database-name>',
        'USER': '<your-username>',
        'PASSWORD': '<your-password>',
        'HOST': '<your-host>',  # For localhost, use 'localhost' or '127.0.0.1'
        'PORT': '3306',  # Default MySQL port
    }
}
```
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## Available Endpoints

### 1. Static HTML Content
Endpoint: http://127.0.0.1:8000/restaurant/

### 2. Token Authentication API
Endpoint: http://127.0.0.1:8000/restaurant/api-token-auth/

Request Body Example:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
Response example:
```json
{
    "token": "abc123exampletoken"
}
```
After obtaining the token via the /api-token-auth/ endpoint, include the token in the Authorization header of subsequent requests:

This will authenticate your API request and allow you to access protected resources.


### 3. Menu Items API

Endpoint: /menu/

Method: GET

Response Example:
``` json
[
    {
        "id": 1,
        "title": "Spaghetti Carbonara",
        "price": "12.50",
        "inventory": 15
    },
    {
        "id": 2,
        "title": "Caesar Salad",
        "price": "8.99",
        "inventory": 25
    }
]
```

Endpoint: /menu/

Method: POST

Request Body Example:
```json
{
    {
    "title": "New Menu Item",
    "price": 9.99,
    "inventory": 25
}
}
```
Response Example:
```json
{
	"id": 2,
	"title": "New Menu Item",
	"price": "9.99",
	"inventory": 25
}
```

Endpoint: /menu/<int:pk>

Method: GET

Response Example:
Response Example:
```json
{
	"id": 2,
	"title": "New Menu Item",
	"price": "9.99",
	"inventory": 25
}


## Testing
python manage.py test
