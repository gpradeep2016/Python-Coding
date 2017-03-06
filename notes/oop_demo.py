''' Goal:  Go deeper into Python's objected oriented programming '''

class Animal:
    'A generic animal class'

    kind = 'critter'
    
    def __init__(self, name):
        self.name = name

class WildThings:

    def jump(self):
        print 'I am jumping'

class Cat(Animal, WildThings):
    'A simple feline class'

    kind = 'feline'

    def talk(self):
        print 'Meow! %s is purring.' % self.name

class Dog(Animal, WildThings):
    'A simple canine class'

    kind = 'canine'

    def talk(self):
        print 'Woof! %s is barking.' % self.name

#################################################

c = Cat('Socks')        
d = Dog('Fido')
e = Dog('Buddy')
f = Dog('Checkers')

pets = [c, d, e, f]
for pet in pets:
    pet.talk()
    
