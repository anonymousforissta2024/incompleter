#Source: https://stackoverflow.com/questions/52465552/builtins-typeerror-typeerror
@app.route('/')
def getAllItems():
    return redirect(url_for('getCategoryItems', category_name='ab', cat_id=1))


@app.route('/<string:category_name>/items/')
def getCategoryItems(category_name, cat_id):
    id = cat_id;
    items = session.query(Item).filter_by(category_id=id).all()
    output = ''
    for item in items:
        output += item.title + '</br>'
    return output