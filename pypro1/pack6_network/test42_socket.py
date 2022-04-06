# 파이썬 네트워크
# 네트워크를 위한 통신 채널 지원: socket 모듈

import socket

print(socket.getservbyname('http','tcp'))   #80
print(socket.getservbyname('telnet','tcp')) #23
print(socket.getservbyname('ftp','tcp'))    #21
print(socket.getservbyname('smtp','tcp'))   #25
print(socket.getservbyname('pop3','tcp'))   #110

print(socket.getaddrinfo('www.naver.com', '80', proto=socket.SOL_TCP))
# 223.130.195.95, 223.130.195.200

