#Source: https://stackoverflow.com/questions/65149626/how-to-correct-typeerror-execute-takes-from-2-to-4-positional-arguments-but-5
if user_input==2:
    number=int(input("Enter number of tickets you want to book-"))
    for b in range(0,number):
        passengername=input("Enter name of passenger-")
        starting_station=input("Enter name of station from where passenger will board train-")
        destination=input("Enter name of station passenger wishes to reach-")
                    
        print("Ticket Booked!")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="railways")
        mycursor=mydb.cursor()
        mycursor.execute("select train_no from route_fare where from_station=%s",(starting_station,), " and to_station=%s",(destination,))
        for w in mycursor:
            train_number_p=w
        