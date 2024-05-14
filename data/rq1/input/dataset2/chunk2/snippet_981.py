#Source: https://stackoverflow.com/questions/51412753/attributeerror-str-object-has-no-attribute-timeud-variable-calling
import timelines
#x(forward-back) Axies
global x
x = 0
#y(left-right) Axies
global y
y = 0
#z(up) Axies
global z
z = 0
#t(time) Axies
global t
t = 0
#u(universe) Axies
global u
u = 1
#how much time moves by per-turn, string
global time_change
time_change = 'doggos'
#the timeline, nets of exctinction
timelines = 'Universal Development\nSolar Development\nPlanetary Development\nEvolution\nIntelligence\nContinental Drift\nSpeech\nReligion/Beliefs\nAgriculture\nTechnological Innovation\nSocial Politics\nCommunities\nCivilizations\nWar/Conflicts\nEconomy\nLaw\n----------------------------------------------'
global loop
def checkAction():
    ca_loop = 1
    while( ca_loop == 1 ):
        if turn_action == 'timeline':
            which_timeline = input("What timeline would you like to view?\n----------------------------------------------\n" + timelines + "\n[Timelines]~| ")
            if which_timeline == "Universal Development":
                print(timelines.TimeUD)
            else:
                print("~|Improper Input|~\n")
def turn1( tc ):
    t = 0
    global turn_action
    while ( loop == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 ):
        t = t + tc
        print("The current " + time_change + "s is " + str(t))
        turn_action = input("~| ")
        checkAction()
        input("~|Press enter to continue to the next Time-Period|~")

loop_select = 1
while ( loop_select == 1 ):
    loop = int(input("~|Choose a time-change per turn|~\n\n~| "))
    if loop == 1:
        print("The time-change is set to miliseconds.\n\n")
        time_change = 'Milisecond'
        loop_select = 0
    elif loop == 2:
        print("The time-change is set to seconds.\n\n")
        time_change = 'Second'
        loop_select = 0
    elif loop == 3:
        print("The time-change is set to minutes.\n\n")
        time_change = 'Minute'
        loop_select = 0
    elif loop == 4:
        print("The time-change is set to hours.\n\n")
        time_change = 'Hour'
        loop_select = 0
    elif loop == 5:
        print("The time-change is set to days.\n\n")
        time_change = 'Day'
        loop_select = 0
    elif loop == 6:
        print("The time-change is set to months.\n\n")
        time_change = 'Month'
        loop_select = 0
    elif loop == 7:
        print("The time-change is set to years.\n\n")
        time_change = 'Year'
        loop_select = 0
    elif loop == 8:
        print("The time-change is set to cosmic seconds.(a really long time)")

        time_change = 'Cosmic Second'
        loop_select = 0
    elif loop == type.str:
        print("~|Improper Input|~")
    else:
        print("Input is currently inapplicable, try again.\n")

if loop == 1:
    turn1( 0.1 )
elif loop == 2 or 3 or 4 or 5 or 6 or 7 or 8:
    turn1( 1 )