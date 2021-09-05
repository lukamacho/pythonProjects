import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "Disconnected!"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)


client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


print("Start Chatting")
input()
print("This was my first message")
while True:
    string = input("Enter some string")
    if string == DISCONNECT_MESSAGE:
        break
    send(string)

