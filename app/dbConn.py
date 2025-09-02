import sqlite3
import os

# Database configuration
db_path = 'temp_db_files/temp_complex.db'  # Path to your SQLite file

# Ensure the directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Create a connection to the database
try:
    conn = sqlite3.connect(db_path)
    print(f"Successfully connected to database: {db_path}")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    conn = None