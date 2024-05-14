#Source: https://stackoverflow.com/questions/63873612/how-come-i-get-childhood-takes-no-arguments-when-i-execute-it-but-when-i-delete
from ex45f import live
class childhood(live):

    def development(self):
        intelligent["low", "average", "high"]
        if random.choice(intelligent) == low:
            return "You are dumb"
        elif random.choice(intelligent) == average:
            return "You are average"
        else:
            return "You are smart"

        if school == "yes" and intelligent == high:
            return 'You will have an fantastic life'
        elif school == "no" and intelligent == high:
            return "You will have an average life"
        elif school == "maybe" and intelligent == high:
            return "You will have an good life"
        elif school == "yes" and intelligent == average:
            return "You will have an good life"
        elif school == "no" and intelligent == average:
            return "You will have an bad life"
        elif school == "maybe" and intelligent == average:
            return "You will have an average life"
        elif school == "yes" and intelligent == low:
            return "You will have an average life"
        elif school == "no" and intelligent == low:
            return "You will have an horrible life"
        else:
            return "You will have an bad life"
#Zoek op how random choice antwoord bij betrekt
like_school = """Do you like school?
Possible answers: yes, no or maybe
> """
school = input(like_school)
q = childhood(school)
q.development()