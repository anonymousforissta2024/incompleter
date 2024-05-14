#Source: https://stackoverflow.com/questions/42751642/py2neo-v3-attributeerror-object-has-no-attribute-db-exists
class Content(GraphObject):             # group Person and Institution
    pass

class Person(Content):
    __primarykey__ = 'name'

    name = Property()
    in_scholar_names = Property()
#   
    mentored = RelatedTo('Person')
    mentored_by = RelatedFrom('Person', 'MENTORED')
    worked_alongside = Related('Person', 'WORKED_ALONGSIDE')
    studied_at = RelatedTo('Institution')
    worked_at = RelatedTo('Institution')
    tagged = RelatedTo('Tag')
    member_of = RelatedTo('Institution')

    last_update = RelatedTo('UpdateLog')

    def __lt__(self, other):
        return self.name.split()[-1] < other.name.split()[-1]

class Institution(Content):
    __primarykey__ = 'name'
#   
    name = Property()
    location = Property()
    type = Property()
    carnegie_class = Property()
#   
    students = RelatedFrom('Person', 'STUDIED_AT')
    employees = RelatedFrom('Person', 'WORKED_AT')
    members = RelatedFrom('Person', 'MEMBER_OF')

    last_update = RelatedTo('UpdateLog')

    def __lt__(self, other):
        return self.name < other.name


class User(GraphObject):
    __primarykey__ = 'username'

    username = Property()
    joined = Property()
    last_access = Property()
    active = Property()

    contributed = RelatedTo('UpdateLog')


class Provenance(GraphObject):          # group UpdateLog and DataSource
    pass    
# 
class UpdateLog(Provenance):
    __primarykey__ = 'id'

    id = Property()
    timestamp = Property()
    query = Property()

    previous = RelatedTo('UpdateLog', 'LAST_UPDATE')
    next = RelatedFrom('UpdateLog', 'LAST_UPDATE')
    based_on = RelatedTo('Provenance', 'BASED_ON')

    affected_nodes = RelatedFrom('Content', 'LAST_UPDATE')
    contributed_by = RelatedFrom('User', 'CONTRIBUTED')

class DataSource(Provenance):
    __primarykey__ = 'uri'

    id = Property()
    description = Property()
    uri = Property()

    source_for = RelatedFrom('UpdateLog', 'BASED_ON')


class Tag(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    description = Property()

    see_also = Related('Tag')
    tagged = RelatedFrom('Content')