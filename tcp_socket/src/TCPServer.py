from socket import *

PORT = 48484
socket = socket(AF_INET, SOCK_STREAM)

# bind? dns/bind? no, binding the port to the socket 
socket.bind(('',PORT))
socket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = socket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close() 