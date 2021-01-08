# This is a Simple TCP Chat application created in Python 3.8
# Designed by Robert Miller

import threading
import socket

host = '127.0.0.1' #localhost
port = 55555

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
            clients.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} Left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break
