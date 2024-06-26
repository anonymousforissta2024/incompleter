#Source: https://stackoverflow.com/questions/41192303/getting-nameerror-variable-not-defined-when-it-is-defined
from survey import AnonymousSurvey

#   Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#   Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)