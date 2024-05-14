#Source: https://stackoverflow.com/questions/58819446/attribute-error-join-object-has-no-attribute-implicit-returning
class Example(Base):
    __tablename__ = 'example'

    id = Column(ForeignKey(u'visit.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True, unique=True)
    startdate = Column(Date, nullable=False)
    enddate = Column(Date)