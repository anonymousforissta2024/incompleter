#Source: https://stackoverflow.com/questions/60127532/no-matter-what-i-do-i-keep-getting-attributeerror-str-object-has-no-attribute
@portfolio_app.route('/postContactForm', methods=['POST'])
def postContactForm():
    #Gets the data sent from frontend  
    ajax_data = json.load(request.data.decode()) 
    print(ajax_data)

    # Connect to DB
    db = connectToDB()

    #Choose collection name
    contact_data = db.contact_data
    print(contact_data)

    #Inserts data into database
    contact_data.insert_one(ajax_data)

    #Returns data to ajax
    return jsonify({'Success it worked'})