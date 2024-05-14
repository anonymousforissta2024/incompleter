#Source: https://stackoverflow.com/questions/66146515/typeerror-when-trying-to-pass-output-of-one-function-to-another-function
import socket
import threading
import subprocess

nickname = input("Choose a nickname: ")
subprocess.run("./ipaddress.sh")

with open("ip_addr.txt", 'r') as f:
    file = f.readline()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((file, 48812))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                pass
            else:
                print(message)

        except:
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()