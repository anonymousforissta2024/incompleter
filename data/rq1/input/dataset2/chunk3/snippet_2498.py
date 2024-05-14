#Source: https://stackoverflow.com/questions/69186111/how-to-solve-could-not-import-todo-schema-schema-for-graphene-setting-schema
urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]