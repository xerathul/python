# 단순 Client
import socket

clientSock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(('127.0.0.1',7878))
clientSock.sendall('hello server'.encode('UTF_8'))
re_msg=clientSock.recv(1024).decode()
print('수신 자료: ',re_msg)
clientSock.close()
