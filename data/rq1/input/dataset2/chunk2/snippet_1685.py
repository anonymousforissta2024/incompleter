#Source: https://stackoverflow.com/questions/56174450/why-do-i-keep-getting-the-attributeerror-str-object-has-no-attribute-student
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5

TRUE = True
FALSE = False

COURSES_INPUT = 'courses-sample.txt'
STUDENTS_INPUT= 'students-sample.txt'

import student
import course 



def main():

    process_students()
    process_courses()
    option = get_option()
    while option != 5:
        if option == 1:

            course_num = input('please input course number of course you wish to add: ')
            add_course = new_student.add_course(course_num)
            while add_course == FALSE:
                print('The course requested for add does not exist. Please Try Again.')
                course_num = input('Please input course number of course you wish to add: ')
            if new_course.space_available() == TRUE:
                new_course.enroll_student()
            else:
                print('Class requested does not have any seats available.')

        if option == 2:
            course_num = input('please input course number of course you wish to drop: ')
            drop_course = new_student.drop_course(course_num)
            while drop_course == FALSE:
                print('The enrolled course requested for drop does not exist. Please Try Again.')
                course_num = input('Please input course number of course you wish to drop: ')
            new_course.drop_student()

        if option == 3:
            print_student_info(student_dict)
        if option == 4:
            print_course_schedule(course_dict)
        option = get_option()
    write_updated('students-updated.txt',student_dict)
    write_updated('courses-updated.txt',course_dict)



def print_menu():
    print("1. Add course")
    print("2. Drop course")
    print("3. Print student's schedule")
    print("4. Print course schedule")
    print("5. Done")
    print("")

def get_option():
    print_menu()
    choice = input("What would you like to do? ")
    while choice not in range(1,6):
        print_menu()
        choice = input("Choice is invalid. What would you like to do? ")
    return choice

def process_students():
    student_dict = {}
    student_info = open(STUDENTS_INPUT,"r")
    for student in student_info:
        info_list = student.split(":")
        new_id = info_list[0]
        first_name = info_list[1]
        last_name = info_list[2]
        course_list = info_list[3:]
        new_student = student.Student(new_id, first_name, last_name, course_list)
        print(new_student.line_for_file())
        student_dict[new_eid] = new_student
    student_info.close()

def process_courses():
    course_dict = {}
    course_info = open(COURSES_INPUT,"r")
    for course in course_info:
        info_list = course.split(";")
        unique_num = info_list[0]
        class_name = info_list[1]
        prof = info_list[2]
        seats = info_list[3]
        capacity = info_list[4]
        new_course = course.Course(unique_num, class_name, prof, seats, capacity)
        course_dict[unique_num] = new_course
    course_info.close()

def print_course_schedule(course_dict):
    for value in course_dict:
        print(value)

def print_student_info(student_dict):
    for value in student_dict:
        print(value)

def get_id():
    eid = input("What is the UT EID? ")
    while eid not in student_dict:
        eid = input("Invalid UT EID. Please re-enter: ")
    return eid

def get_unique():
    unique = input("What is the course unique number? ")
    while unique not in course_dict:
        unique = input("Invalid unique number. Please re-enter: ")
    return unique


def write_updated(filename,dictionary):
    output_file = open(filename,'w')

    for key in dictionary:
        output_file.write(dictionary[key])
    output_file.close()
main()