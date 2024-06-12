import socket
from generate_keys import keys_generator

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
    print(client_public_key)
    break
