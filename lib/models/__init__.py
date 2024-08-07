import sqlite3

CONN = sqlite3.connect('my_database.db')
CURSOR = CONN.cursor()
# Check if the connection is successful
if CONN:
    print("Database connection successful.")
else:
    print("Failed to connect to the database.")
