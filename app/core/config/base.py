import os

DB = {
    'DIALECT': os.getenv('DB_DIALECT', 'mariadb+mariadbconnector'),
    'HOST': os.getenv('DB_HOST', 'mariadb'),
    'PORT': int(os.getenv('DB_PORT', 3306)),
    'NAME': os.getenv('DB_NAME', 'auth'),
    'USER': os.getenv('DB_USER', 'developer'),
    'PASSWORD': os.getenv('DB_PASSWORD', '123'),
}
