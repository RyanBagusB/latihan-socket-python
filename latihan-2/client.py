import socket

port = 7000
s = socket.socket()
s.connect(('127.0.0.1', port))
print(s.recv(1024))
s.send('Hello from client'.encode())
s.close()