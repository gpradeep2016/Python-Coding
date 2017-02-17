
class base_class(object):
    ''' This is the parent class and this is called base class. We will be inheriting this call in another calls
    so that will be the derived class'''

    def __init__ (self):
        print " This is the base class\n"

x = base_class()


class derived_class(base_class):
    '''This is the derived class and we inherit the base class in this '''

    def __init__(self):
        base_class.__init__(self)
        print " This is the derived class"


y = derived_class()
