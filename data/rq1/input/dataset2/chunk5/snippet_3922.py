#Source: https://stackoverflow.com/questions/39841881/typeerror-python-unit-testing-using-mock
session = scoped_session(sessionmaker(bind=db_state.engine))
@use_kwargs({
    'user_id': fields.Integer(location='json', required=True)
})
def create_user(user_id):
    with session as s:
        try:
            result = user_dao.create_user(s, user_id)
            return json.dumps(result), 200, {'Content-Type': 'application/json; charset=utf-8'}
        except SQLAlchemyError:
            result = {"Fatal": "Id not found"}
            return json.dumps(result), 404, {'Content-Type': 'application/json; charset=utf-8'}