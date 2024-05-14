#Source: https://stackoverflow.com/questions/28182582/typeerror-does-not-support-the-buffer-interface-twitch-irc-chat-bot
import socket #imports module allowing connection to IRC
import threading #imports module allowing timing functions

bot_owner = 'BetterFollowerBot'
nick = 'BetterFollowerBot'
channel = '#BetterFollowerBot'
server = 'irc.twitch.tv'
password = '~Took This Out~'

queue = 0 #sets variable for anti-spam queue functionality

irc = socket.socket()
irc.connect((server, 6667)) #connects to the server

#sends variables for connection to twitch chat
irc.send('PASS ' + password + '\r\n')
irc.send('USER ' + nick + ' 0 * :' + bot_owner + '\r\n')
irc.send('NICK ' + nick + '\r\n')
irc.send('JOIN ' + channel + '\r\n') 

def message(msg): #function for sending messages to the IRC chat
    global queue
    queue = queue + 1
    print (queue)
    if queue < 20: #ensures does not send >20 msgs per 30 seconds.
        irc.send('PRIVMSG ' + channel + ' :' + msg + '\r\n')
    else:
        print ('Message deleted')

def queuetimer(): #function for resetting the queue every 30 seconds
    global queue
    print ('queue reset')
    queue = 0
    threading.Timer(30,queuetimer).start()
queuetimer()

while True:
    data = irc.recv(1204) #gets output from IRC server
    user = data.split(':')[1]
    user = user.split('!')[0] #determines the sender of the messages
    print (data)

    if data.find('PING') != -1:
        irc.send(data.replace('PING', 'PONG')) #responds to PINGS from the server
    if data.find('!test') != -1: #!test command
        message('Hi')