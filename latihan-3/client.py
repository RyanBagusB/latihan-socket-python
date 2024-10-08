import socket
import threading

host = '127.0.0.1'
port = 7000

alias = input("Input your name >>> ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "alias?":
                client.send(alias.encode("utf-8"))
            else:
                print(message)
        except:
            print("Error")
            client.close()
            break

def client_send():
    while True:
        message_form_client = input("")
        message = f"{alias}: {message_form_client}"
        client.send(message.encode("utf-8"))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
