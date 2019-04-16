import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/crypto')
secret = os.getenv('SECRET', 'secret')
