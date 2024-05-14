#Source: https://stackoverflow.com/questions/66194956/typeerror-contact-got-an-unexpected-keyword-argument-name-while-using-flask
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        '''Add entry to the database'''
        Name = request.form.get('Name')
        Email = request.form.get('Email')
        Phone = request.form.get('Phone_no')
        Message = request.form.get('Msg')
        entry = contact(name=Name, email=Email, phone_no=Phone, msg=Message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')