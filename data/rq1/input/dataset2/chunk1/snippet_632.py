#Source: https://stackoverflow.com/questions/54279772/filenotfounderror-errno-2-no-such-file-or-directory-ubuntu
with open('./folder/tickets.csv', 'w', encoding='utf-8') as ouf:
    for i in d:
        i = str(i)
        ouf.write(i + '\n')