#Source: https://stackoverflow.com/questions/54161685/dont-understand-why-this-attributeerror-occurs-in-for-loop
class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

q_dict = [
    """Q1 Why is it important to scan your target network slowly?\n
    A. To avoid alerting the IDS
    B. It is not necessary to scan the network slowly."""'\n\n\n',

    """Q2 What is the difference between a traditional firewall and an IPS?
    A. Firewalls do not generate logs.
    D. IPS can dissect packets"""'\n\n\n',

    """Q3 What tool is able to conduct a man-in-the-Middle Attack on an 802.3 environment?
    A. Ettercap
    B. Cain & Abel"""'\n\n\n'
]

a_dict = [
    Questions(q_dict[0], "A"),
    Questions(q_dict[1], "D"),
    Questions(q_dict[2], "B")
]

def start(a_dict):
    points = 0
    for question in a_dict:
        answer = input(q_dict.question)
        if answer == a_dict.answer:
            points += 10
    print("You got 10 points")
    print("Total points: %s" % points)

start(a_dict)