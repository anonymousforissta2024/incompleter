#Source: https://stackoverflow.com/questions/72254923/python-attributeerror-object-has-no-attribute-pointing-to-constructor-error
from Employee import Employee
from Student import Student
from CustomExceptions import InvalidAge
from CustomExceptions import InvalidYearsWorked
from CustomExceptions import InvalidUnits

# Try/except block
try:
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = int(input("Enter age: "))
    job_skills = input("Enter job skills: ")
    yrs_worked = float(input("Enter years worked: "))

    # create an instance of an emplpoyee person
    my_person = Employee(name, address, age, job_skills, yrs_worked)

    # invoke the to_string() method and display everything
    print(my_person.to_string())

    name = input("\nEnter name: ")
    address = input("Enter address: ")
    age = int(input("Enter age: "))
    major = input("Enter major: ")
    units_completed = float(input("Enter units completed: "))

    # create an instance of a student person
    my_person = Student(name, address, age, major, units_completed)

    # invoke the to_string() method and display everything
    print(my_person.to_string())

# Exception handling, always go from most specific exception to most generic
except InvalidAge as e:
    print("Invalid age: ", e)
except InvalidYearsWorked as e:
    print("Invalid years worked: ", e)
except InvalidUnits as e:
    print("Invalid units completed: ", e)

# generic exception
#except Exception as ex:
    print("Generic exception: ", ex)