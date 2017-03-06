''' Learn to common argument passing patterns in Python

    Rule:  required arguments go before optional arguments
'''

def mypow(base, exp):
    'Raise a base to the power of exp'
    return base ** exp

print mypow(2, 5)                       # Positional arguments --> Order matters.
print mypow(exp=5, base=2)              # Keyword arguments --> The Name matters.
print mypow(2, exp=5)                   # Hybrid arguments --> Positional go before keywords

arguments = (2, 5)                      # Cheap, compact, fast luggage --> Tuple
print mypow(arguments[0], arguments[1])
print mypow(*arguments)                 # 1 star UNPACKS any SEQUENCE into POSITIONAL args

arguments = {'exp': 5, 'base': 2}       # Nice, heavy, expensive luggage --> Dict
print mypow(exp=arguments['exp'], base=arguments['base'])
print mypow(**arguments)                # 2 stars UNPACKS any MAPPING into KEYWORD args

def f(a, b, c=0, d=0):                  # Defaults arguments
    return a + b + c + d

def f(a, b, *args, **kwargs):           # 1 star PACKS extra POSITIONAL args into a TUPLE
    print a                             # 2 star PACKS extra KEYWORD args into a DICT
    print b
    print args
    print kwargs

def logging_pow(*args, **kwargs):
    'Wrap the mypow() function to add input and output logging for debugging'
    print 'mypow() called with %r and %r' % (args, kwargs)
    answer = mypow(*args, **kwargs)
    print 'the answer is %r' % answer
    return answer

y = logging_pow(2, 5)
y = logging_pow(exp=5, base=2)
y = logging_pow(2, exp=5)
