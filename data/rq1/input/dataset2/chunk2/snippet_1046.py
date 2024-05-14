#Source: https://stackoverflow.com/questions/15005488/python3-3-typeerror-embedded-nul-character
class Page(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    name = Column(String(40, convert_unicode=True), unique=True)
    data = Column(String(40, convert_unicode=True))

    def __init__(self, name, data):
        self.name = name
        self.data = data


class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit') ]
    def __init__(self, request):
        pass