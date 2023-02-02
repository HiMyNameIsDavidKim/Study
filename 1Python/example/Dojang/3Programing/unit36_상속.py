class Animal():
    def eat(self):
        print('eat')

class Wing():
    def flap(self):
        print('flap')

class Bird(Animal, Wing):
    def fly(slef):
        print('fly')

if __name__ == '__main__':
    b = Bird()
    b.eat()
    b.flap()
    b.fly()
    print(issubclass(Bird, Animal))
    print(issubclass(Bird, Wing))