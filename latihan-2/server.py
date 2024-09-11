import socket

port = 7000
s = socket.socket()
print("Socket successfully created")

s.bind(('', port))
print(f"Socket listening on port: {port}")

s.listen(5)
print("Socket is listening...")

while True:
    c, addr = s.accept()
    print(f"Got connection from {addr}")
    message = ("Thank you for connecting")
    c.send(message.encode())
    print(c.recv(1024))
    c.close()