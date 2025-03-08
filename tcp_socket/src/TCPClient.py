from socket import *

serverName = '127.0.0.1'
serverPort = 48484
clientSocket = socket(AF_INET, SOCK_STREAM)

def connect_socket(serverName, serverPort): 
    try: 
        clientSocket.connect((serverName,serverPort))

    except: 
        print("unable to connect")


def socket_send(sentence): 
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)

    print('From Server: ', modifiedSentence.decode())

connect_socket(serverName, serverPort)
sentence = input('Input lowercase sentence:')
socket_send(sentence)
clientSocket.close()