import socket

HOST, PORT = '127.0.0.1', 1488

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
    if client: break
