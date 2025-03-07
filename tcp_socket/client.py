from socket import *

"""
socket library
- 
"""

serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

def connect_socket(serverName, serverPort): 
    try: 
        clientSocket.connect((serverName,serverPort))

    except: 
        print("unable to connect")


def socket_send(): 
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)

    print('From Server: ', modifiedSentence.decode())


sentence = input('Input lowercase sentence:')
clientSocket.close()