#coding:utf-8

from encodings import utf_8
import socket 
import threading

class ThreadForClient(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        print(data)
        
host, port=('', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Server is Launched ...")

while True:
    socket.listen()
    conn, address = socket.accept()
    print("Client is Connected")
    my_thread = ThreadForClient(conn)
    my_thread.start() 

conn.close()
socket.close()