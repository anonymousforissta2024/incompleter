#Source: https://stackoverflow.com/questions/65500142/how-do-i-fix-this-python-nameerror
import os

# starting values for day, month and year
parent_dir = 'C:\\Users\\locale\\Desktop\\DIRS\\'
day_int = 16
month_int = 9
year_int = 2020


def gen_day_str():
    if len(str(day_int)) == 1:
        day_str = '0' + str(day_int)
    elif len(str(day_int)) == 2:
        day_str = str(day_int)
    else:
        print('error! exiting...')
        exit()
def gen_month_str():
    if len(str(month_int)) == 1:
        month_str = '0' + str(month_int)
    elif len(str(month_int)) == 2:
        month_str = str(month_int)
    else:
        print('error! exiting...')
        exit()
def gen_year_str():
    year_str = str(year_int)
def gen_dir_name():
    gen_day_str()
    gen_month_str()
    gen_year_str()
    dir_name = day_str + '-' + month_str + '-' + year_str


while day_int <= 30:
    gen_dir_name()
    os.mkdir(parent_dir + dir_name)
    day_int += 1
day_int = 1
month_int = 10
while day_int <= 16:
    gen_dir_name()
    os.mkdir(parent_dir + dir_name)
    day_int += 1

print('folders created successfully!')
exit()