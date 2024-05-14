#Source: https://stackoverflow.com/questions/77441584/attributeerror-tuple-object-has-no-attribute-split-options-list-using-pick
with open(str(option)[2:-2], 'r') as quiz:
    quiz_info = [line.strip() for line in quiz]
    quiz_title = str(option)
    title = '-----------\n QUIZZABLE \n-----------\n   Quiz    \n-----------\n\nQuiz:', quiz_title
    quiz_question_total = quiz_info[0]
    quiz_score = 0
    quiz_question_count = int(1)
    quiz_current_line = int(1)
    while quiz_question_count <= int(quiz_question_total):
        quiz_question = quiz_info[int(quiz_current_line)]
        quiz_current_line = int(quiz_current_line) + int(1)
        quiz_question_option_count = quiz_info[int(quiz_current_line)]
        quiz_current_line = int(quiz_current_line) + int(1)
        quiz_question_option = int(1)
        options = []
        while quiz_question_option <= int(quiz_question_option_count):
            options += [quiz_info[int(quiz_current_line)]]
            quiz_current_line = int(quiz_current_line) + int(1)
            quiz_question_option = int(quiz_question_option) + int(1)
        quiz_question_answer = quiz_info[int(quiz_current_line)]
        quiz_current_line = int(quiz_current_line) + int(1)
        option, index = pick(options, title, indicator='[>]', default_index=0)    #problem
        if option == quiz_question_answer:
            quiz_score = quiz_score + int(1)