from socket import *

# can either use IP or the hostname
# if hostname is used, dns lookup is automatically performed 
HOST = "127.0.0.1"
PORT = 12000

def create_socket(): 
    try: 
        clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
        return clientSocket
    except: 
        # print(f"{p}")
        return None

def run(): 

    message = input("Enter the message you want to send (lowercase): ")
    socket = create_socket()
    if socket is not None: 
        # converts from string to byte (for serialization?)
        # takes a tuple of the destination address
        socket.sendto(message.encode(), (HOST, PORT))
    else: 
        return 
    
    # the udp server returns the message and its address
    # are we defining the recvfrom function? no
    # what is the structure of the serverAddress? IP and port?
    # we provide the buffer size of the input 
    # this is the buffer size in the IO stream? its a buffered IO?
    # this is working in a similar way to that of cache
    modifiedMessage, serverAddress = socket.recvfrom(2048)
    print(f"Here is the response from the server: {modifiedMessage.decode()}")
    socket.close()


if __name__ == "__main__": 
    run()