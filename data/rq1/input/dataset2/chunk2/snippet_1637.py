#Source: https://stackoverflow.com/questions/60315844/typeerror-pagination-object-is-not-iterable-in-flask
@api.route('/', methods=["GET"])
@app.route('/page/<int:page>')
class List(Resource):
    """USER data(s)"""

    def get(self, page=1):
        """GET Lists"""
        all_data = User.query.paginate(page, per_page=2)
        result = user_serializer.dump(all_data)
        return result