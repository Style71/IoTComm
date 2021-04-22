from socket import *

#SERVER_IP = 'localhost'
SERVER_IP = '43.129.87.211'
SERVER_PORT = 11111
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

CLIENT_IP = 'localhost'
CLIENT_PORT = 4484
CLIENT_ADDR = (CLIENT_IP, CLIENT_PORT)

BUFSIZ = 1024

tcpClientSock = socket(AF_INET, SOCK_STREAM)
# tcpClientSock.bind(CLIENT_ADDR)
tcpClientSock.connect(SERVER_ADDR)

print('Connect to ' + SERVER_IP + '/'+str(SERVER_PORT)+'.')
while True:
    data = input('> ')
    if not data:
        break
    tcpClientSock.send(bytes(data, 'utf-8'))
    data = tcpClientSock.recv(BUFSIZ)
    if not data:
        break
    print(str(data, encoding='utf-8'))

tcpClientSock.close()
