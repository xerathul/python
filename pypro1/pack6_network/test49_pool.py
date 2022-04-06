# thread는 GIL 이라는 매커니즘 때문에 완전한 멀티 프로세싱이 불가.
# 멀티 프로세싱을 위한 Pool, Process를 별도 지원

#Pool 클래스

from multiprocessing import Pool

import time
import os

def pool_func(arg):
    print('값', arg, '에 대한 pid: ',os.getpid()) # 현재 실행되는 process id를 출력
    time.sleep(1)
    return arg+10

#pool_func(2)
#print(pool_func(2))

if __name__=='__main__':
    startTime=int(time.time())
    '''
    #방법 1: Pool 객체 사용 x 함수 호출
    for i in range(10):
        print(pool_func(i))
    
    endTime=int(time.time())
    print('총 작업 시간: ',(endTime-startTime))
    '''
    #방법 2: Pool 객체 사용 함수 호출
    po= Pool(processes=4) #3-5를 권장
    print(po.map(pool_func,range(10)))
    
    endTime=int(time.time())
    print('총 작업 시간: ',(endTime-startTime))
    