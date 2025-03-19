import os
from dotenv import load_dotenv

# Load .env file
load_dotenv(dotenv_path=".env")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "source_db": os.getenv("DB_NAME_SOURCE"),
    "target_db": os.getenv("DB_NAME_TARGET")
}

# Debugging: Print values to verify correct loading
print("Database Config:", DB_CONFIG)
print("DB_NAME_SOURCE:", repr(os.getenv("DB_NAME_SOURCE")))  # ✅ Show hidden characters
