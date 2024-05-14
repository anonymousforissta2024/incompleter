#Source: https://stackoverflow.com/questions/75966522/attributeerror-function-object-has-no-attribute-args
from flask import Flask, request
from flask import Flask, render_template
from flask_paginate import Pagination, get_page_parameter
import mysql.connector

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'test'

db = mysql.connector.connect(user=app.config['MYSQL_USER'], password=app.config['MYSQL_PASSWORD'],
                             host=app.config['MYSQL_HOST'], database=app.config['MYSQL_DB'])
cursor = db.cursor()

@app.route('/')
def thumbnails():
    # Retrieve the image URLs from the database
    cursor.execute('SELECT * FROM sheet1')
    rows = cursor.fetchall()
    
   
    
    # Paginate the image URLs
    page = int(request.args.get['page']) if 'page' in request.args else 1
    per_page = 12
    offset = (page - 1) * per_page
    pagination = Pagination(page=page, per_page=per_page, total=len(image_urls), css_framework='bootstrap4')
    image_urls = image_urls[offset:offset+per_page]
    
 
    
    # Pass the image URLs and pagination object to the template
    return render_template('index.html', rows=rows,pagination=pagination)



if __name__ == "__main__":
    app.run(debug=True,port=5000)