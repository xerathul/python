# 시각화 : 많은 양의 데이터를 효율적으로 봄으로써, 인사이트를 정확하게 얻어 낼 수 있다..

import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='malgun gothic')  #한글깨짐 방지
plt.rcParams['axes.unicode_minus']= False   #마이너스 깨짐 방지

x=['서울','인천','수원']  #set x
y=[5,3,7]

#plt.plot(y)
'''
plt.xlim([-1,3])    #축 경계값 지정
plt.ylim([0,10])    
plt.yticks(list(range(0,11,3)))
plt.plot(x,y)
plt.show()  #plot을 열 때 주피터에서는 안써도 됨


data = np.arange(1,11,2)
print(data)
plt.plot(data)
x=range(5)
print(x)
for a, b in zip(x, data):
    plt.text(a, b, str(b))
plt.show()


#sin 곡선
x = np.arange(10)
y= np.sin(x)
print(x,y)
#plt.plot(x, y)
#plt.plot(x, y,'bo') #blue, 동그라미
#plt.plot(x, y,'r+')
plt.plot(x, y, 'go--',linewidth=2, markersize =12) #linewidth=2 => lw=2, marker='o', c='g'
plt.show()

#hold

x= np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(figsize=(10,5))
plt.plot(x, y_sin, 'r')
plt.scatter(x, y_cos)
plt.xlabel('x축')
plt.ylabel('y축')
plt.legend(['sin','cosin'])
plt.show()



# subplot
x= np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2,1, 1) #2행 1열 포커스=1행
plt.plot(x, y_sin, 'r')
plt.title('사인그래프')

plt.subplot(2,1,2)
plt.scatter(x, y_cos)
plt.title('코사인그래프')
plt.show()

'''

#꺾은 선 그래프
irum = ['a','b','c','d','e']
kor = [80,50,70,70,90]
eng = [60,70,80,70,60]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bs-.')
plt.title('시험점수')
plt.ylim([0,100])
plt.legend(['국어','영어'], loc = 4)
plt.grid(True)


fig = plt.gcf()     #그래프를 이미지로 저장
plt.show()

fig.savefig('plot.png')

from matplotlib.pyplot import imread
img = imread('plot.png')
plt.imshow(img)
plt.show()