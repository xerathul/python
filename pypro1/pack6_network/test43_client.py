# 단순 Client
from socket import *

clientSock= socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1',8888))
clientSock.send('hello world'.encode('UTF_8','strict'))
clientSock.close()