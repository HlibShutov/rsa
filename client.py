import socket
from generate_keys import keys_generator

HOST, PORT = '127.0.0.1', 1488
keys = keys_generator()
public_key, private_key = keys[0], keys[1]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    print('connected to server')
except:
    print('error while connecting to server')

while True:
    message = client.recv(124)
    public_server_key = message.decode()
    print(public_server_key)
    client.send(bytes(' '.join(list(map(str, public_key))), 'utf-8'))
    if message: break
