#Source: https://stackoverflow.com/questions/65918421/typeerror-anonimoussurvey-takes-0-positional-arguments-but-1-was-given
def AnonimousSurvey():
    
    def __init__(self, question):
        
        self.question = question
        self.responses = []
        
    def show_question(self):
        print(self.question)
        
    def store_response(self, new_response):
        self.responses.append(new_response)
        
    def show_result(self):
        print("Survay results:")
        for i in self.responses:
            print("- " + i)
quest = "hello what is your name?"
new_surv = AnonimousSurvey(quest)
new_surv.show_question()