#Source: https://stackoverflow.com/questions/61161498/why-binary-usage-in-sqlalchemy-with-python3-cause-a-typeerror-string-argument
from sqlalchemy import MetaData, Integer, Column, Table, Binary, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DB_CONFIG = {
        'user': 'user_test',
        'password': 'PSW_test',
        'host': '127.0.0.1',
        'database': 'db_test',
        }

if __name__ == '__main__':
    Base = declarative_base()
    engine = create_engine("mysql+mysqlconnector://%(user)s:%(password)s@%(host)s/%(database)s" % DB_CONFIG,
                           echo=False)
    Base.metadata.bind = engine
    db_sessionmaker = sessionmaker(bind=engine)
    Session = scoped_session(db_sessionmaker)

    # create the table
    meta = MetaData()
    tests = Table(
        'test', meta,
        Column('id', Integer, primary_key=True),
        Column('attr', Binary)
    )
    meta.create_all(engine)


    class Test(Base):
        __tablename__ = 'test'
        id = Column(Integer, primary_key=True)
        attr = Column(Binary)

    new_test = Test(attr='try'.encode('utf-8'))
    session = Session()
    session.add(new_test)
    session.commit()
    result = session.query(Test).all()
    for a in result:
        print(a, a.id, a.attr)
    Session.remove()