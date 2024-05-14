#Source: https://stackoverflow.com/questions/35998854/sqlalchemy-tablename-nameerror
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Collection(Base):
    __tablename__ == 'Collection'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Sheet(Base):
    __tablename__ = 'sheet'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    collection_id = Column(Integer, ForeignKey('collection.id'))

def main():
    base_name = 'test.db'
    engine = create_engine('sqlite:///{}'.format(base_name))
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()