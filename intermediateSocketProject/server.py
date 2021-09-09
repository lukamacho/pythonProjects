# This is a sample Python script.
import pickle
import socket
from _thread import *
import sys
from game import Game


server = socket.gethostbyname(socket.gethostname())
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except:
    print("Something happened")


s.listen()
print("Waiting for a client to connect the server")


connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset_game()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break;

    print("Lost connection.")
    try:
        del games[gameId]
        print("Closing game", gameId)
    except:
        pass

    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to ", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2

    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("New game created")
    else:
        games[gameId].ready = True
        p = 1
    start_new_thread(threaded_client(), (conn, p, gameId))
