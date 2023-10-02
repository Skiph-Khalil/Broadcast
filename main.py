import sys


def print_python_version():
    print(sys.version)
import socket

# Server configuration
# Host ipv4
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345     # Port to listen on
BUFFER_SIZE = 1024

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

# Store connected client sockets
client_sockets = [5]

# Accept incoming client connections
while True:
    client_conn, client_addr = server_socket.accept()
    print(f"Connected by {client_addr}")
    
    # Store the client socket for broadcasting
    client_sockets.append(client_conn)

    # Handle messages from this client in a separate thread or process

# Function to broadcast a message to all connected clients
def broadcast(message):
    for client_socket in client_sockets:
        try:
            client_socket.send(message.encode())
        except Exception as e:
            # Handle exceptions such as client disconnection
            print(f"Error broadcasting to {client_socket}: {str(e)}")

# Example usage:
while True:
    message = input("Hi")
    broadcast(message)

import socket

# Client configuration
# Replace "server ip address" with Ipv4
SERVER_HOST = 'server_ip_address'
SERVER_PORT = 12345
BUFFER_SIZE = 1024

# Create a socket to connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Function to receive and display messages from the server
def receive_messages():
    while True:
        try:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            print(data.decode())
        except Exception as e:
            # Handle exceptions such as server disconnection
            print(f"Error receiving message: {str(e)}")
            break

# Start a separate thread or process to receive and display messages
# You can use threading or multiprocessing for this purpose

# Example usage:
receive_messages()
