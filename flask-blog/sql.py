import sqlite3

with sqlite3.connect('blog.db') as conn:
    c = conn.cursor()
    c.execute("""CREATE TABLE posts
            (title TEXT, post TEXT)""")
    c.execute('INSERT INTO posts VALUES("Good", "I\'m Good!")')
    c.execute('INSERT INTO posts VALUES("Happy", "I\'m Happy!")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m Okay!")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m Excellent!")')

