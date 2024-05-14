#Source: https://stackoverflow.com/questions/56018370/typeerror-type-object-does-not-support-item-assignment
userlist = dict


def main():
    add_user()
    print(userlist)


def add_user():
    global new_user
    global new_password
    print('Please indicate your desired username')
    new_user = str(input('User: ')).lower
    print('Please indicate your desired password')
    new_password = str(input('Password: '))
    print('Please re-enter your password')
    password_addcheck = str(input('Password:'))
    if password_addcheck == new_password:
        print('Thank you, you are now successfully registered')
        userlist[new_user] = new_password
    else:
        print('Password does not match, please repeat process')
        add_user()


main()