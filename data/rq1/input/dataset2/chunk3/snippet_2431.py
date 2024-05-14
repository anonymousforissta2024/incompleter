#Source: https://stackoverflow.com/questions/69186111/how-to-solve-could-not-import-todo-schema-schema-for-graphene-setting-schema
class Query(TodoQuery, graphene.ObjectType):
    pass


class Mutation(Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)