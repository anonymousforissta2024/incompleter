#Source: https://stackoverflow.com/questions/57548878/getting-a-typeerror-unhashable-type-list
user = input('Name any1 who is near to you ').split(',')
friends_open = open('friends.txt', 'r')
friends_read = friends_open.readlines()
friends_open.close()

near_by  = []
near_by.append(user)

setting_near = set(near_by)
setting_friends = set(friends_read)

intersect = setting_near.intersection(setting_friends)

for n in intersect:
    print(f'your {intersect} friend is here!! meet him ')