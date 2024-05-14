def check(string, sub_str):
    if string.find(sub_str) == -1:
        print('NO')
    else:
        print('YES')
string = 'geeks for geeks'
check(string, sub_str)