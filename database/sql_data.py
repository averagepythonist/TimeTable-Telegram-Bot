import peewee

db = peewee.SqliteDatabase(r'/Users/gennadiy/PycharmProjects/timetable_bot/database/data.db')

class Base(peewee.Model):
    class Meta:
        database = db

class Data(Base):
    user = peewee.CharField(primary_key=True)
    time = peewee.CharField()
    group = peewee.CharField()