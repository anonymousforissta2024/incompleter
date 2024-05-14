#Source: https://stackoverflow.com/questions/59536926/typeerror-module-takes-at-most-2-arguments-3-given-code-taken-from-pluralsi
import student as student

students = []


class HighSchoolStudent(student):

    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a High School student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"

...