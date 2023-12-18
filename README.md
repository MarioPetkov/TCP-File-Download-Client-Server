# TCP File Download Client-Server
 This project demonstrates a simple client-server file download implementation using the TCP protocol in Python. 
 The server allows clients to request and download files from a specified directory.

Getting Started
Prerequisites
Make sure you have Python installed on your machine.

Installation
1. Clone the repository:
git clone https://github.com/MarioPetkov/TCP-File-Download-Client-Server.git
2. Navigate to the project directory:
cd TCP-File-Download-Client-Server

Usage
1. Run the server:
python server.py
Replace '127.0.0.1' and 12345 in server.py with the desired server IP address and port.
2. Run the client:
python client.py
The client will prompt you to enter the filename you want to download. 
The downloaded file will be saved in the same directory as the client.py script.

Customization
1. Server Configuration: You can customize the server IP address, port, and base path in the server.py script.
2. Client Configuration: You can customize the server IP address and port in the client.py script. Additionally, you can modify the filename prompt to suit your needs.

Acknowledgments
This project is a basic implementation for educational purposes.
Inspiration: Project "Introduction Data Network" classes.

Feel free to contribute, report issues, or suggest improvements!