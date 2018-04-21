"""
Explore SQLite functionalty
"""
import sqlite3

# connect with given DB otherwise create new database
conn = sqlite3.connect('cars.db')

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table with given column
cursor.execute("""CREATE TABLE inventory
                (make TEXT, model TEXT, quantity INT)
                """)

# close the database connection
conn.close()
