import socket

HOST, PORT = '127.0.0.1', 1488
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    print('connected to server')
except:
    print('error while connecting to server')
