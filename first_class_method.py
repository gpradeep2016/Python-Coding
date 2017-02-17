class first_class(object):

    ''' This creates a new class named First_class'''

    pi = 3.14

    ''' This is a class variable and defined outside all methods'''

    def __init__ (self, radius):
        ''' This is a special method called class constructor or initialization method used to create a new instance of class'''
        self.radius = radius
        pass



    def display_dia(self):
        ''' This creates a new object attribute '''
        return  self.radius ** 2

x = first_class(5)

''' Here we are creating an instance of a class named first_class. Here x is an object of class "first_object" '''

print x.radius
print x.display_dia()

x.age = 10
''' here age is an attribute and we can add or remove attributes any time '''

print x.age
