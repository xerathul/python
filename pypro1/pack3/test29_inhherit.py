#자원의 재활용을 목적으로 클래스의 상속 - 다형성

class Animal:
    def __init__(self):
        print('Animal 생성자')
    def move(self):
        print('움직이는 생물')
    
    #...
class Dog(Animal):
    def __init__(self): #자식의 생성자가 있을경우 부모의 생성자를 호출하지 않음- 자식의 생성자가 없을 경우 부모의 생성자 수행
        print('Dog 생성자')
        
    def my(self):
        print('난 댕댕이! >3<')

dog1= Dog()
dog1.move()
dog1.my()

print()
class Horse(Animal):
    pass

horse1=Horse()
horse1.move()