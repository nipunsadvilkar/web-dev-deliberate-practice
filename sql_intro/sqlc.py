"""
Insert many values into DB using parameterized statements
"""
import sqlite3

# connect with given DB and commit changes without explicitly calling
# commit function
with sqlite3.connect('new.db') as conn:
    # get a cursor object used to execute SQL commands
    cursor = conn.cursor()
    cities = [
            ('Boston', 'MA', 34325235),
            ('Houston', 'TX', 1244143),
            ('CHICAGO', 'IL', 9324053),
            ('PHOENIX', 'AZ', 2343225)
            ]
    # insert data into table with parameterized statements i.e., ? placeholder
    # string substitution is deprecated since it may cause SQL injections
    # where user supplies value which looks like a SQL statement and may cause
    # reveal sensitive information or even damage or destroy the DB
    cursor.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

# close the database connection
conn.close()
