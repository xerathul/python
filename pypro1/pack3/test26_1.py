# Singer Type 객체
#abc라는 가수 객체

import pack3.test26
from pack3.test26 import Singer


abc= pack3.test26.Singer()
print('타이틀 송: ',abc.title_song)
abc.sing()
abc.title_song='tudutudu'
abc.sing()
abc.hello()

#------------아래 내용은 별도의 모듈을 만들었다 가정---------------
bts=Singer()
bts.sing()

