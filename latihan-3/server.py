import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 7000
clients = []
aliases = []
server_running = True

server.bind((host, port))
server.listen()

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f"{alias.decode('utf-8')} has left the chat".encode("utf-8"))
            aliases.remove(alias)
            break

def receive():
    global server_running
    while server_running:
        try:
            print("Server is running and listening...")
            client, address = server.accept()
            print(f"Client with IP Address: {str(address)} has joined")
            client.send("alias?".encode("utf-8"))
            alias = client.recv(1024)
            clients.append(client)
            aliases.append(alias)
            print(f"The alias of the client is {alias.decode('utf-8')}")
            client.send("You are now connected!".encode("utf-8"))
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()
        except:
            break

def stop_server():
    global server_running
    while True:
        command = input("")
        if command.lower() == "exit":
            print("Stopping the server...")
            server_running = False
            server.close()
            break

if __name__ == "__main__":
    # Thread for receiving clients
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    # Thread for stopping the server
    stop_thread = threading.Thread(target=stop_server)
    stop_thread.start()

    # Wait for both threads to finish
    receive_thread.join()
    stop_thread.join()
