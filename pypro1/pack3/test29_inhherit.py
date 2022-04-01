#자원의 재활용을 목적으로 클래스의 상속 - 다형성

class Animal:
    def __init__(self):
        print('Animal 생성자')
    def move(self):
        print('움직이는 생물')
    
    #...
class Dog(Animal):
    def __init__(self):
        print('Dog 생성자')
        
    def my(self):
        print('난 댕댕이! >3<')

dog1= Dog()
dog1.move()
dog1.my()
