
def my_square():
    while True:
        try:
            num = int(raw_input ('please enter a number'))
        except:
            print "Looks like you did not enter a number"
            continue
        else:
            final_num = num ** 2
            print final_num
            break


my_square()
