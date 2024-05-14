#Source: https://stackoverflow.com/questions/59291245/flask-login-attributeerror-int-object-has-no-attribute-is-authenticated
@app.route('/device_detail', methods=['GET', 'POST'])
@login_required
def device_detail_operation():
    error = None
    return render_template('device_detail.html', error=error)