from socket import *

# define the address
HOST = "127.0.0.1"
PORT = 12000

def create_socket(): 
    try: 
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        return clientSocket
    except: 
        # print(f"{p}")
        return None

def run(): 
    socket = create_socket()

    if socket is not None:

        # 
        socket.bind(('', PORT))
        print('The server is ready to receive')

        while True: 
            message, clientAddress = socket.recvfrom(2048)
            modifiedMessage = message.decode().upper()
            socket.sendto(modifiedMessage.encode(), clientAddress)

run()