import socket
from generate_keys import keys_generator
from decrypt import decrypt
from encrypt import encrypt

HOST, PORT = '127.0.0.1', 1488

keys = keys_generator()
public_key, private_key = keys[0], keys[1]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((HOST, PORT))
    print(f"server started on {HOST}:{PORT}")
except:
    print(f"error while starting server on {HOST}:{PORT}")

server.listen(5)

while True:
    client, address = server.accept()
    print(f"user connected on address: {address[0]}:{address[1]}")
    client.send(bytes(' '.join(list(map(str,public_key))), 'utf-8'))
    client_public_key = client.recv(124).decode()
    client_public_key = list(map(int, client_public_key.split(' ')))
    print(client_public_key)
    message = list(map(int, client.recv(124).decode().split(' ')))
    print(decrypt(private_key, message))
    message = input()
    message = encrypt(client_public_key, message)
    client.send(bytes(message, "utf-8"))
