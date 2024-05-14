#Source: https://stackoverflow.com/questions/66146515/typeerror-when-trying-to-pass-output-of-one-function-to-another-function
import threading
import socket
import subprocess

subprocess.run("./ipaddress.sh")

with open("ip_addr.txt", 'r') as f:
    file = f.readline()

host = file
port = 48812

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode('ascii'))
            nicknames.remove(nickname)
            break
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with{str(address)}")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client is {nickname}\n")
        broadcast(f'{nickname}joined the chat!\n'.encode('ascii'))
        client.send("Connected to the server!\n".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is listening...")
receive()