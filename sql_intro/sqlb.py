"""
Explore SQLite functionalty
"""
import sqlite3

# connect with given DB and commit changes without explicitly calling
# commit function
with sqlite3.connect('new.db') as conn:
    # get a cursor object used to execute SQL commands
    cursor = conn.cursor()
    cursor.execute("INSERT INTO population VALUES('DALLAS', \
            'TX', '42000')")
    cursor.execute("INSERT INTO population VALUES('MICHIGAN', \
            'IL', '60000')")

# close the database connection
conn.close()
