from socket import *
from time import ctime
from os import system

#HOST = ''
#HOST = '43.129.87.211'
HOST = '10.0.0.11'
#HOST = '0.0.0.0'
PORT = 4464
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

print('Listening at port '+str(PORT)+'...')
tcpClientSock, addr = tcpServSock.accept()
print('Connect from: %s/%u' % (addr[0], addr[1]))
system('netstat -nap | grep %s:%u' % (addr[0], addr[1]))
tcpClientSock.send(bytes('[%s]Connect to server %s/%u (inner IP/port)' %
                   (ctime(), HOST, PORT), 'utf-8'))

while True:
    data = str(tcpClientSock.recv(BUFSIZ), encoding='utf-8')
    if not data:
        break
    tcpClientSock.send(bytes('[%s]%s' % (ctime(), data), 'utf-8'))

tcpClientSock.close()
tcpServSock.close()
