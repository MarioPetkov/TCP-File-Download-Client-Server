import socket
import threading
import os

def handle_client(client_socket, base_path):
    # Receive the filename from the client
    filename = client_socket.recv(1024).decode('utf-8')
    file_path = os.path.join(base_path, filename)

    # Check if the file exists
    if os.path.exists(file_path) and os.path.isfile(file_path):
        # Send the file size to the client
        file_size = os.path.getsize(file_path)
        client_socket.send(str(file_size).encode('utf-8'))

        # Receive acknowledgment from the client before sending the file
        client_socket.recv(1024)

        # Send the file to the client
        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)
    else:
        # If the file doesn't exist, send an error message to the client
        client_socket.send(b'File not found')

    # Close the connection
    client_socket.close()

def start_server(host, port, base_path):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, base_path))
        client_handler.start()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    BASE_PATH = '/Users/miopi/Desktop/SoftUni/project/server_side'  # Replace with the actual path

    start_server(HOST, PORT, BASE_PATH)
