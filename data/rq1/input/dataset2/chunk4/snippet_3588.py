#Source: https://stackoverflow.com/questions/71897761/python-getopt-module-error-nameerror-name-opts-is-not-defined-after-importi
import getopt
import sys
    
   
question_id= None
arg_student = None
argv = sys.argv[1:]
print("test")

try:
    opts, args = getopt.getopt(argv, "i:s:", ["question_id=","arg_student="])
except:
    print("Error")

for opt, arg in opts:
    if opt in ['-i', '--question_id']:
        question_id = arg
    elif opt in ['-s', '--arg_student']:
        arg_student = arg

print("Question Number: " + question_id)        
print("Student response: " + arg_student)