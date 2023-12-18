import socket
import os

def download_file(host, port, filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Send the filename to the server
    client.send(filename.encode('utf-8'))

    # Receive the file size or an error message from the server
    response = client.recv(1024).decode('utf-8')

    if response.isdigit():
        file_size = int(response)
        # Send acknowledgment to the server before receiving the file
        client.send(b'OK')

        # Set the download path to the current directory
        download_path = os.path.join(os.path.dirname(__file__), filename)

        # Receive and save the file
        with open(download_path, 'wb') as file:
            data = client.recv(1024)
            total_received = len(data)
            file.write(data)
            while total_received < file_size:
                data = client.recv(1024)
                total_received += len(data)
                file.write(data)
        print(f"[*] File '{filename}' downloaded successfully to '{download_path}'")
    else:
        print(f"[!] {response}")

    # Close the connection
    client.close()

if __name__ == "__main__":
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 12345

    file_to_download = input("Enter filename to download: ")

    download_file(SERVER_HOST, SERVER_PORT, file_to_download)
