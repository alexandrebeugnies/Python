#coding:utf-8

import socket


try:
    host, port = ('127.0.0.1', 5566)
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    print("Client Connected !")

    data = "Hello , I'm the Client"
    data = data.encode("utf8")
    socket.sendall(data)
except ConnectionRefusedError:
    print("Server Connection Failed")
finally:
    socket.close()
