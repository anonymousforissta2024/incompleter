#Source: https://stackoverflow.com/questions/74308258/getting-nameerror-name-leader-is-not-defined-what-does-this-mean
if sad == 1:
    if fear == 0 and leader == 1 and known == 1:
        print("Congrats, you are the 'Foolish Leader'1/13")
elif fear == 1 and leader == 1 and known == 0:
    print("Congrats, you are the 'Smart, yet scared Leader'2/13")
elif fear == 0 and leader == 1 and known == 0:
    print("Congrats, you are the 'Smart Leader'3/13")
elif fear == 1 and leader == 0 and known == 1:
    print("Congrats, you are the 'Scared Fool'4/13")
elif sad == 1 and coward == 1:
    print("Congrats, you are the 'Sad Coward'5/13")
elif fear == 1 and coward == 1:
    print("Congrats, you are the 'Scared Coward'6/13")
elif sad == -1:
    if mind_changed == 1:
        print("Congrats, you can't make up your mind.7/13")
elif mind_changed == 0:
    print("Congrats, you can make up your mind.8/13")
elif insane == 1:
    print("Congrats, you are a horrible person and I never want to see you again.9/13")
elif lazy == 1:
    print("Congrats, you are lazy.10/13")
elif suic == True:
    print("I hope that you're ok.11/13")
elif envy == 1:
    print("Congrats, you're a good person.12/13")
elif fear == 1:
    print("Congrats, you're scared easily.13/13")

if suic == True:
    print("I hope you're ok.... Due to you choosing 'C' on the Multiple Choice, I suggest you stop playing.?/13")