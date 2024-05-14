#Source: https://stackoverflow.com/questions/28112952/attributeerror-tuple-object-has-no-attribute-encode-when-inserting-data-usi
import mysql.connector

# ...

# Connect to MySQL Database and send user_input data to 'user' TABLE.
cnx = mysql.connector.connect(user='root', password='ash123', host='localhost', database='user_data_db')
cursor = cnx.cursor()

query = ("INSERT INTO user (user_id, first_name, last_name, age, postcode,  email_address)"
         "VALUES (%s, %s, %s, %s, %s, %s)", (user_id, firstname, lastname, age, postcode, email)) 

cursor.execute(query)
print("Executed Successfully")

cursor.close()
cnx.close()