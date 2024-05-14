#Source: https://stackoverflow.com/questions/69186111/how-to-solve-could-not-import-todo-schema-schema-for-graphene-setting-schema
# declar todo model field
class TodoType(DjangoObjectType):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'date', 'text')


# declar user model filed
class UserType(DjangoObjectType):
    class Meta:
        model = User


# todo list query
class TodoQuery(graphene.ObjectType):
    todoList = DjangoListField(TodoType)

    def resolve_todoList(root, info):
        return TodoList.objects.filter(userId=2)


# create todo
class TodoCreate(graphene.Mutation):
    class Arguments:
        title = graphene.String(Required=True)
        text = graphene.string(Required=True)

    todo = graphene.Field(TodoType)

    def mutate(root, info, title, text):
        # userId = info.context.user
        user = User.objects.get(id=2)
        todo = TodoList(userId=user, title=title, text=text)
        todo.save()
        return TodoCreate(todo=todo)


# todo mutation
class Mutation(graphene.ObjectType):
    createTodo = TodoCreate.Field()