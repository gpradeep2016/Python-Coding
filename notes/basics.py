''' Quick tour of Python '''

# Dictionary
owner = {}
owner['pc'] = 'rachel'
owner['mac'] = 'raymond'
owner['vtech'] = 'matthew'

print owner
print len(owner)
print 'mac' in owner
print 'lenovo' in owner

print owner.keys()
print owner.values()
print owner.items()

del owner['mac']
owner['vtech'] = 'tom'
print owner

# Lists

parts = ['opamp', '555 timer', '7404']
for part in parts:                       # Iterable
    print 'I have a', part
print parts[0]

try:
    print parts[50]
except IndexError:                       # Exception handling
    print 'There is no part 50'
print 'Done'

newlist = [parts[0], parts[1]]
newlist = parts[0:2]                     # Slicing

parts.sort()
parts.reverse()
print parts

parts.append('voltage regulator')
print parts
print parts.pop()                        # append and pop implement a LIFO stack

# Function definitions

def cube(x):
    'Return a value times itself thrice'
    return x ** 3

print cube(11)

def family(lastname, first_names):
    'Display the family members in a nice tabular format'
    print 'The %s Family' % lastname.title()
    print '=' * (len(first_names) + 11)
    for name in first_names:
        print '* %s' % name.title()
    print

family('simpsons', ['homer', 'marge', 'bart', 'lisa', 'maggie'])
family(first_names=['mike', 'marcia', 'greg', 'jan', 'peter', 'cindy', 'bobby'], lastname='brady')
    
# class definitions

class Interconnection:
    'Show the pin requirements for a PC board'

    def __init__(self, board_name='Unknown'):
        self.board_name = board_name
        self.connections = {}

    def add_pin(self, pin, connection):
        'Record a new pin connection requirement'
        self.connections[pin] = connection

    def check_pin(self, pin, connection):
        'Verify a pin connection requirement'
        return self.connections[pin] == connection

prototype = Interconnection('Active low pass filter')
prototype.add_pin(12, 'Vcc +5V')
prototype.add_pin(8, 'Ground 2amps max')
prototype.add_pin(5, 'Signal 8 ohms')

print 'Specs for:', prototype.board_name
print prototype.check_pin(12, 'Vcc +5V')

# Files

with open('notes/hamlet.txt') as f:
    play = f.read()
print len(play)
print play[0:400]

# Urls

import urllib

u = urllib.urlopen('http://www.jython.org')
page = u.read()
print page[0:400]
