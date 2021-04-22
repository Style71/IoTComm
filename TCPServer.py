from socket import *
from time import ctime

HOST = ''
PORT = 11111
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

print('Establish TCP server at port '+str(PORT)+', waiting for connection...')
tcpClientSock, addr = tcpServSock.accept()
print('...connected from: ', addr)
tcpClientSock.send(bytes('[%s]' % (ctime()), 'utf-8'))

while True:
    data = str(tcpClientSock.recv(BUFSIZ), encoding='utf-8')
    if not data:
        break
    tcpClientSock.send(bytes('[%s]%s' % (ctime(), data), 'utf-8'))

tcpClientSock.close()
tcpServSock.close()
