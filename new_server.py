import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host = socket.gethostname()
port = 5000
ThreadCount = 0

import mysql.connector

# create connection object
con = mysql.connector.connect(
host="localhost", user="root",
password="", database="College")

# create cursor object
cursor = con.cursor()

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(2)
def multi_threaded_client(connection,info):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        # print(info)
        connection.sendall(str.encode(info))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    query1 = str("select * from student")
    cursor.execute(query1)
    table = cursor.fetchall()
    data1 = ""
    for row in range(ThreadCount*5,ThreadCount*5+5):
        data1 += str(table[row]) + "\n"
    start_new_thread(multi_threaded_client, (Client, data1))

    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()