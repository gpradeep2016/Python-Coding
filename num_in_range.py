def range_check(num,low,high):
    ''' This function checks if a number is in a given range including the high and low'''
    return num in range(low, high+1)

# Need to use a if statement to check
# if num in range (low,high+1)
 #       print "num is in the range"
  #  else:
   #     print "num not in rang
#
#
#

test = range_check(5,2,10)
print test

