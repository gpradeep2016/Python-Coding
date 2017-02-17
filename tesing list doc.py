def find_prime(num):
    '''This function is to find prime numbers from 1 to 100'''
    for x in range(2,num):
        if num % x  == 0:
            print "%s is not prime" % (num)
            break
        else:
            print "%s is prime" % (num)
            break

find_prime(14)



even = lambda num: num % 2 == 0
even (4)
