# 클래스는 새로운 타입을 만든다.
class Singer:
    title_song='화이팅 코리아'
    
    def sing(self):
        msg=' 노래는 '
        print(msg,self.title_song, 'lala~')
    #...
    def hello(self):
        print('안녕하세요 이번 싱글은', self.title_song,' 입니다!')

#------------아래 내용은 별도의 모듈을 만들었다 가정---------------
bts=Singer()
bts.sing()
bts.hello()

print()
blackpink= Singer()
blackpink.hello()
blackpink.sing()
blackpink.title_song='tudutudu'
blackpink.sing()
blackpink.co='YG'
print('소속사',blackpink.co)

# print('소속사',bts.co) error
bts.sing()
print()
print(id(bts),id(blackpink))

print((type(bts),type(blackpink)))
