#Source: https://stackoverflow.com/questions/71450772/flask-pytest-failed-tests-test-data-response-pytest-post-data-response-type
@discovery_bp.route('/', methods=['GET', 'POST'])
def search_fund():
    """ 
    Given function creates a text field for search box &
    renders on index.html then 
    retrieves input data from the user, run that data through 
    function query_fund from data.py to grab the fund 
    & renders back onto index.html 
    """
    form = SearchForm()
    if form.validate_on_submit():
        query = form.search.data.split(" ")
        fund_results = query_fund(query, f"{FUND_STORE_API_HOST}/{FUND_ENDPOINT}")
        return render_template("search.html", query =query, 
                              fund_results = fund_results,
                              form=form)
    return render_template("search.html", form=form)    