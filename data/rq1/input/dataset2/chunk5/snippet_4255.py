#Source: https://stackoverflow.com/questions/48721067/global-variable-in-python-getting-nameerror-while-performing-a-comparison
import xml.sax

class Employee :
    def __init__(self, id):
        self.id = id


class EmployeeHandler(xml.sax.ContentHandler):

    emp = None
    emplist = []
    fName = False
    lName = False
    age = False
    company = False

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        print("startElement '" + name + "'")

        if name == "Employees" :
            global emplist
            emplist = []

        if name == "Employee":
            global emp
            emp = Employee(attrs.getValue("id"))
        elif name == "FirstName":
            global fName
            fName = True
        elif name == "LastName":
            global lName
            lName = True
        elif name == "Age":
            global age
            age = True
        elif name == "Company":
            global company
            company = True

    def characters(self, content):
        print("characters '" + content + "'")
        global fName, lName, age, company
        if fName is True:
            emp.firstName = content
        elif lName is True:
            emp.lastName = content
        elif age is True:
            emp.age = content
        elif company is True:
            emp.company = content



    def endElement(self, name):
        print("endElement '" + name + "'")
        if name == "Employee":
            #global emplist : To use list methods global is not required
            emplist.append(emp)


def main(sourceFileName):
    source = open(sourceFileName)
    xml.sax.parse(source, EmployeeHandler())


if __name__ == "__main__":
    main("EmployeeData")
    print("Ids ", emplist[0].id , emplist[1].id)