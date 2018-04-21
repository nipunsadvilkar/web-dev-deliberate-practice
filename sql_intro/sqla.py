"""
Explore SQLite functionalty
"""
import sqlite3

# connect with given DB otherwise create new database
conn = sqlite3.connect('new.db')

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table with given column
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)

cursor.execute("INSERT INTO population VALUES('NEW YORK CITY', \
        'NY', '8200000')")
cursor.execute("INSERT INTO population VALUES('SAN FRANCISCO', \
        'CA', '8000000')")

conn.commit()

# close the database connection
conn.close()
