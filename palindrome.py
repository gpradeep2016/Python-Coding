def palindrome(input_string):
    """Checks is a string is palindrome or not"""
    if input_string [::-1] == input_string:
        """ [:]     grabs everything
            [:x]    grabs everything up to but not including x
            [::1]   grabs everything in step size of 1 (basically grabs the whole string)
            [::-1]  grabs everything in step size of -1 ( basically grabs the string in reverse order) """
        print input_string, "is a Palindrome"
    else:
        print input_string, "is not a Palindrome"



palindrome ("malayalam")