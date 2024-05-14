#Source: https://stackoverflow.com/questions/56506781/how-to-fix-typeerror-if-no-direction-is-specified-key-or-list-must-be-an-inst
@app.route('/search')
def search():
    """Route for full text search bar"""
    page_limit = 6 #Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    db_query = request.args['db_query']
    total = mongo.db.recipe.create_index({'$text': {'$search': db_query }})
    t_total = len([x for x in total])
    pages = range(1, int(math.ceil(t_total / page_limit)) + 1)
    results = mongo.db.recipe.find({'$text': {'$search': db_query }}).sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template('search.html', results=results, pages=pages, current_page=current_page, db_query=db_query)