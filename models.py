from peewee import *

db = SqliteDatabase('database.db')


class User(Model):
    Name = TextField(unique=True, null=False)
    PhoneNumber = TextField(null=False)
    Age = DecimalField(default=0)
    Course = TextField(null=False)

    class Meta:
        database = db


db.create_tables([User])
