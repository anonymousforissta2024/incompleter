#Source: https://stackoverflow.com/questions/55764232/typeerror-write-object-cannot-be-interpreted-as-an-integer-write-is-the-na
from xlwt import Workbook
import random
import string


class write_to_excel():



    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    def randomString(stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))


s = write_to_excel()
r = s.randomString()
print(r)