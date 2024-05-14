#Source: https://stackoverflow.com/questions/66086091/peewee-query-typeerror-not-supported-between-instances-of-modelcompounds
class People(Model):
    name = CharField()
    parent = ForeignKeyField('self', backref='children', null=True, on_delete='CASCADE')