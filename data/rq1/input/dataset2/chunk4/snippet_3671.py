#Source: https://stackoverflow.com/questions/60761057/typeerror-nonetype-object-is-not-iterable-even-though-it-is-set
import random
import time


def login():
    while True:
        username = input('What is your username? ')
        password = input('What is your password? ')
        if username not in ('User1', 'User2', 'User3', 'User4', 'User5'):
            print('Incorrect username, try again')
            continue

        if password != "pwd":
            print('Incorrect password, try again')
            continue

        print(f'Welcome, {username} you have been successfully logged in.')
        return username


def roll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    change = 10 if (die1 + die2) % 2 == 0 else -5
    points = die1 + die2 + change
    if die1 == die2:
        points += random.randint(1, 6)
    return points


def game(user1, user2):
    player1_points = 0
    player2_points = 0
    for i in range(1,5):
        player1_points += roll()
        print(f'After this round {user1} you now have: {player1_points} Points')
        time.sleep(1)
        player2_points += roll()
        print(f'After this round {user2} you now have: {player2_points} Points')
        time.sleep(1)

    player1TieBreak = player1_points
    player2TieBreak = player2_points
    if player1_points == player2TieBreak:
        player1TieBreak = random.randint(1,6)
        player2TieBreak = random.randint(1,6)
        if player1TieBreak > player2TieBreak:
            return (player1_points, player1_win), (player2_points, not player2_win)
        else:
            return (player2_points, player2_win), (player1_points, not player1_win)


def add_winner(winner):
    with open('Winner.txt', 'a') as f:
        f.write('{winner[0]},{winner[1]}\n')


def get_leaderboard():
    with open('Leaderboard.txt', 'r') as f:
        return [line.replace('\n','') for line in f.readlines()]


def update_leaderboard(leaderboard, winner):
    for idx, item in enumerate(leaderboard):
        if item.split(', ')[1] == winner[1] and int(item.split(', ')[0]) < int(winner[0]):
                leaderboard[idx] = '{}, {}'.format(winner[0], winner[1])
        else:
            pass
    leaderboard.sort(reverse=True)


def save_leaderboard(leaderboard):
    with open('Leaderboard.txt', 'w') as f:
        for item in leaderboard:
            f.write(f'{item}\n')


def main():
    user1 = login()
    user2 = login()
    (player1, player1_win), (player2, player2_win) = game(user1, user2)
    if player1_win:
        winner = (player1, user1)
    else:
        winner = (player2, user2)
    print('Well done, {winner[1]} you won with {winner[0]} Points')
    add_winner(winner)
    leaderboard = get_leaderboard()
    update_leaderboard(leaderboard, winner)
    save_leaderboard(leaderboard)



main()