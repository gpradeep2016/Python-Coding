import string

def check_if_pangrams(str, alphabet=string.ascii_lowercase):
    '''Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example : "The quick brown fox jumps over the lazy dog" '''
    for char in alphabet:
        if char.lower() not in str:
            print str, "is not a pangram"
            break
        elif char == "z":
            print str, "is a pangram"








check_if_pangrams("The quick brown fox jumps over the lazy dog")