# Thread 를 이용한 날짜 및 시간 출력 
import time

now= time.localtime()
print(now.tm_year, now.tm_mon, now.tm_mday)

import threading

def calendar_show():
    now= time.localtime()
    print('현재는 {}년 {}월 {}일 {}시 {}분 {}초 입니다. '.format(now.tm_year,now.tm_mon,now.tm_mday
                                                     ,now.tm_hour,now.tm_min, now.tm_sec))
    
#calendar_show()

def myRun():
    while True:
        now2= time.localtime()
        if now2.tm_min == 9:break
        
        calendar_show()
        time.sleep(1)
        
th= threading.Thread(target= myRun)
th2= threading.Thread(target= myRun)

th.start()

th.join()

print('프로그램 종료')