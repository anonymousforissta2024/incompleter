#Source: https://stackoverflow.com/questions/53995821/typeerror-str-object-is-not-callable-when-making-a-peewee-model
db = SqliteDatabase("scores.db")


class Score(Model):
    save = CharField()
    score = IntegerField()

    class Meta:
        database = db