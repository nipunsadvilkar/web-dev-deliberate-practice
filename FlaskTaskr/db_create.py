from flasktaskr import db
from flasktaskr.models import Task, User
from datetime import date

# create the database and the db table
db.create_all()

# insert data
db.session.add(User('admin123', 'admin@gmail.com', 'admin123', 'admin123'))
db.session.add(Task('Finish this tutorial', date(2018, 3, 13), 10, date(2018, 3, 13), 1, 1))
db.session.add(Task('Finish Real Python', date(2018, 3, 13), 10, date(2018, 3, 13), 1, 1))

# commit the changes
db.session.commit()
