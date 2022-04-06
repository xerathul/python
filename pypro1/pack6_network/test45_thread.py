# Thread 운영
# process는 실행 가능한 파일을 말한다. 프로세스는 현재 실행 중인 프로그램을 의미하면 task라고도 부른다.
# process 의 작은 실행단위를 thread라고 한다. thread 기법을 이용하면 여러 개의 thread를 통해 여러 개의 작업을 할 수 있다.
# multi thread에 의한 mutil tasking이 가능하다.

import threading, time
def run(id):
    for i in range(1,11):
        print('id:{}-->{}'.format(id,i))
        time.sleep(0.5)

#1) thread x
#run('one') # 순차적
#run('two')

# 2) thread o

th1= threading.Thread(target= run, args=('one',))
th2= threading.Thread(target= run, args=('two',))

th1.start()
th2.start()

print('프로그램 종료')