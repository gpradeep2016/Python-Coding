
def upper_lower_count(input_str):
    x = 0
    y = 0
    for char in input_str:
       if char.islower():
           x = x + 1
       elif char.isupper():
            y = y + 1

    print "Number of upper case characters : %s " % (x)
    print "Number of upper case characters : %s " % (y)


upper_lower_count("Hello Mr. Rogers, how are you this fine Tuesday?")