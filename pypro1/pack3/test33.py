#다중상속 연습문제

class Animal:
    def move(self):
        pass

class Dog(Animal): #단일상속
    name='개'
    def move(self):
        print('개는 왈왈')

class Cat(Animal):
    name='고양이'
    def move(self):
        print('냥이는 야옹')
    
class Fox(Cat, Dog):
    def move(self):
        print('여우는 닝닝니니니닌이이니이인')
    def foxMethod(self):
        print('fox 고유 메소드')

class Wolf(Dog, Cat):
    pass
dog= Dog()
dog.move()
print()
cat= Cat()
cat.move()
print()
wolf=Wolf()
wolf.move()
print()   
fox= Fox()
fox.move()

print()
print(Wolf.__mro__) #class 탐색 순서