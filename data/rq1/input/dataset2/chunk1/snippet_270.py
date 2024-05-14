#Source: https://stackoverflow.com/questions/25491328/typeerror-when-creating-a-wtform-with-mongoengine-and-flask
class Post(database.Document):
    author = database.StringField(
        default='David Y. Stephenson', max_length=255, required=True
    )
    body = database.StringField(required=True)
    comments = database.ListField(
        database.EmbeddedDocumentField('Comment')
    )
    slug = database.StringField(max_length=255, required=True, unique=True)
    tease = database.StringField(max_length=255, required=True)
    time = database.DateTimeField(
        default=datetime.datetime.now, required=True
    )
    title = database.StringField(max_length=255, required=True, unique=True)