#Source: https://stackoverflow.com/questions/46776974/sqlalchemy-1-2-attributeerror-list-object-has-no-attribute-session
from sqlalchemy.orm import sessionmaker
from .models import Deals, db_connect, create_deals_table

class Test(object):

    def __init__(self, args):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def add_item(self):

        session = self.Session()

        tester = Deals(title="test 3 deal",location='here', price=2.00)
        session.add(tester)
        session.commit()