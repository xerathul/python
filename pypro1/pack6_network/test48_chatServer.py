# Multi Chatting Server: Using Socket and thread

import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ss.bind(('127.0.0.1', 5555))
ss.listen(5) #5명만 접속할 수 있는것 아님, 동시에 5명 접속 가능
print('채팅 서버 서비스 시작...')

users=[] #채팅 접속 컴퓨터의 소켓의 개수만큼 담아두기

def chatUser(conn):
    name= conn.recv(1024) 
    data= '^#^ '+name.decode("UTF_8")+'님 입장 ^#^'
    print(data)
    #print(users)
    try:
        for p in users:
            p.send(data.encode("UTF_8")) #모든 접속자에게 채팅명 뿌리기
        
        while True: #모든 접속자의 메세지 주고 받기
            msg = conn.recv(1024) 
            data= name.decode("UTF_8") + "님: "+ msg.decode('UTF_8')
            print(data)
            for p in users:
                p.send(data.encode("UTF_8"))
            
    except Exception as e:
        #print('err: ',e)
        users.remove(conn) #채팅을 종료한 클라이언트 소켓을 제거
        data="---"+ name.decode('UTF_8')+' 님이 퇴장해뚬 ㅠㅠ'
        print(data)
        if users:
            for p in users:
                p.send(data.encode('UTF_8'))
        else:
            print('다 나감')
    
while True:
    conn, addr= ss.accept()
    users.append(conn)
    th = threading.Thread(target=chatUser,args=(conn,))
    th.start()
    
    
    



