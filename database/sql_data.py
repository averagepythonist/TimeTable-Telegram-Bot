import peewee

db = peewee.SqliteDatabase(r'/Users/gennadiy/PycharmProjects/timetable_bot/database/data.db')

class Base(peewee.Model):
    class Meta:
        database = db

class Data(Base):
    user = peewee.IntegerField(primary_key=True)
    time = peewee.CharField()
    group = peewee.CharField()

def check_user(id):
    try:
        check = Data.get(Data.user == id).user
    except peewee.DoesNotExist:
        (Data.create(user=id, time = '7:00', group = 'False'))

def update_time(id, time):
    (Data.update({Data.time : time}).where(Data.user == id)).execute()
    return time

def check_time_is_not_null(id, time):
    try:
        check = Data.get(Data.time == time).time
        return True
    except peewee.DoesNotExist:
        (Data.create(user=id, time=time, group='False'))
        return True







if __name__ == '__main__':
    db.create_tables([Data])