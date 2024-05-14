#Source: https://stackoverflow.com/questions/50048804/name-error-in-python3-when-name-is-defined
#Module 4 project
#4/25/18
#Henry Degner
#This project is meant to determine whether or not certain people are qualified to go to an exclusive concert

#create function askAge, which will use an input statement and comparison operators to see if the user is old enough
def askAge():
    age = int(input("How old are you? "))
    if( age >= 18 ):
        ageReq = "true"
    elif( age < 18 ):
        ageReq = "false"
    else:
        print("Please print you're age with only numerical characters, in years")
        age = int(input("How old are you? "))
#create function askHearing, yes or no question to do you have sensitive hearing
def askHearing():
    hearing = str(input("Do you have sensitive hearing? "))
    if( str(hearing) == "yes","y" ):
        hearingReq = "do"
    elif( str(hearing) == "no","n"):
        hearingReq = "don't"
    else:
        print("Please type yes, or y, if you have sensitivehearing. If not, type no or n.")
        hearing = str(input("Do you have sensitive hearing? "))
#create function askTicket, yes or no question to do you have a ticket
def askTicket():
    ticket = str(input("Do you have a ticket for the concert? "))
    if( str(ticket) == "yes","y" ):
        ticketReq = "do"
    elif( str(ticket) == "no","n"):
        ticketReq = "don't"
    else:
        print("Please type yes if you have a ticket, or no if you don't.")
        ticketReq = str(input("Do you have a ticket for the concert"))
#create function askFun, yes or no question to are you willing to have an awesome time
def askFun():
    fun = str(input("Are you willing to have a great time?"))
    if( str(fun) == "yes","y"):
        funReq = "do"
    elif( str(fun) == "no","n" ):
        funReq = "don't"
    else:
        print("Please type 'yes' or 'no'")
        fun = str(input("Are you willing to have a great time?"))
#use def main():
def main():
#print situation, will ask some questions to see if you can attend concert
    print("Welcome to the Henry Degner Concert Venue! We have to ask you a few questions before we let you into the venue.")
#use askAge
    askAge()
#use askHearing
    askHearing()
#use askTicket
    askTicket()
#use askFun
    askFun()
#print user's answers
    print("You said you are " + age + " years old, you " + hearingReq + " have sensitive hearing, you " + ticketReq + " have a ticket, and you " + funReq + " want to have a great time!")
#use if-else statement, if all three conditions match requirements, print you can attend concert. If not, print you can't attend

#use main()
main()