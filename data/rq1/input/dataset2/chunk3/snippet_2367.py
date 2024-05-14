#Source: https://stackoverflow.com/questions/62749290/how-to-use-add-a-descriptor-to-catch-and-raise-typeerror-upon-attribute-fetches
...
class ArticleField:

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content
...