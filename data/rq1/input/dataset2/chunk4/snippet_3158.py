#Source: https://stackoverflow.com/questions/44138754/python-3-error-typeerror-unsupported-operand-types-for-int-and-str
Billy = {
  'Homework':[76, 88, 90, 95, 54],
  'Quiz':[89, 97, 54],
  'Test':[78, 89]
}

Martha = {
  'Homework':[74, 66, 90, 100, 98],
  'Quiz':[67, 80, 99],
  'Test':[88, 98]
}

Robert = {
  'Homework':[89, 76, 65, 99, 87],
  'Quiz':[88, 98, 73],
  'Test':[81, 92]
}

#Sum
def grades_sum(homework):
    total = 0
    for grade in homework: 
        total += grade
    return total

print(grades_sum(Billy))

#Average
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average