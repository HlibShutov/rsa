import socket
from generate_keys import keys_generator
from encrypt import encrypt
from decrypt import decrypt

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
    public_server_key = list(map(int, public_server_key.split(' ')))
    print(public_server_key)
    client.send(bytes(' '.join(list(map(str, public_key))), 'utf-8'))
    message = input()
    message = encrypt(public_server_key, message)
    client.send(bytes(message, "utf-8"))
    message = list(map(int, client.recv(124).decode().split(' ')))
    print(decrypt(private_key, message))
