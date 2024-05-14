#Source: https://stackoverflow.com/questions/58814134/why-typeerror-is-showing-while-storing-fetchone-value
@app.route('/', methods=['GET', 'POST'])
def index():
    recur_next = ''
    if request.method == 'POST' and request.form['btn']=='XYZ':
        date = request.form['date']
        subject = 'Event'
        reminders='Placement Drive'
        cur = mysql.connection.cursor()
        search = cur.execute('SELECT DATE,SUBJECT,DESCRIPTION,RECUR_NEXT FROM set_reminder WHERE DATE=%s AND SUBJECT=%s AND DESCRIPTION=%s',(date,subject,reminders))
        data = cur.fetchall()
        a = cur.fetchone()
        recur_next = a['RECUR_NEXT']
        print(recur_next)
        cur.close()

    return '''<form method="post">
    <input type="date" name="date">
    <input type="submit" name="btn" value="XYZ">
    </form>'''