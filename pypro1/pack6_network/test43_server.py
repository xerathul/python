# 단순 Echo Server 운영

from socket import *

serverSock= socket(AF_INET, SOCK_STREAM) #socket(소켓 종류, 소켓유형)
serverSock.bind(('127.0.0.1',8888)) #tupleType 이 주소의 저 포트번호를 타고 바인딩
serverSock.listen(1) #client에 연결 정보 수 (1-5)
print('server Start...') 

conn, addr= serverSock.accept()
print('client addr: ',addr)
print('message from client: ',conn.recv(1024).decode())
conn.close()
serverSock.close()

