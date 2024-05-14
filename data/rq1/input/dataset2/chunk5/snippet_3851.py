#Source: https://stackoverflow.com/questions/58819446/attribute-error-join-object-has-no-attribute-implicit-returning
session.begin()
i = sqlalchemy.insert(Example)
i = i.values({'id': 1, 'startdate': 1570798620, 'enddate': 1572526620})
session.execute(i)
session.commit()