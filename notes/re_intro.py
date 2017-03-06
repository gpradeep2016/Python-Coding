''' 
Regular Expression Notes
------------------------

Basics
======
abcd                Exact match
a.cd                Dot matches any one character     axcd   (Note: this is affected by DOTALL)
[aeiou]             Match any one lowercase vowel
[^aeiou]            Match anything that isn't a lower vowel  (Note: the caret must immediately follow the left bracket)
[A-Za-z0-9,]        Character ranges  [ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,]
abc|def             Match either abc or def


Quantifiers (how many to match)
================================
a+                  One or more      a{1,}
a?                  Zero or one      a{0,1}
a*                  Zero or more     a{0,}
a{m,n}              From m to n, inclusive

Make these non-greedy with an extra question mark
a+?
a*?
a{m,n}?


Short-cuts for common character ranges
======================================================
\s                  [ \n\t\f\r]    Any space character
\S                  [^ \n\t\f\r]   Any non-space
\w                  [A-Za-z0-9_]   Wrong!              ==> [A-Za-z'-]+
\W                  [^A-Za-z0-9_]  More Wrong!    
\d                  [0-9]          Any digit
\D                  [^0-9]         Any non-digit


Match by position
=================
\b                  word boundary
^                   beginning of string
$                   end of string


Most common re functions:
===============================================================
re.findall(pattern, string)  --> all matching strings in a list
re.finditer(pattern, string) --> iterator over matching objects
re.search(pattern, string)   --> match object or None
re.match(pattern, string)    --> match object or None
re.sub                       --> substitution and replacing


Match objects
=============
start()
end()
span()
group(0)
groups()


Numbered Groups
===============

 mo = re.search(r'(\d+)/(?:\d+)?/(\d+)', '12/31/2015')
                                  ^-- mo.group(2)               # second sub-grou
                          ^---------- doesn't count as a group        
                    ^---------------- mo.group(1)               # first sub-group
                    |---------------| mo.group(0)               # entire match 

If you don't want a group in parentheses to count as a numbered group
then prefix the group with "?:"

    mo = re.search(r'(?:scored)? (\d+) point', hist)
    print mo.group(1)   # the number will always be group 1
                        # even if the optional "scored" is present
    

Hints:
======
    * patterns should raw strings r''
    * always start with findall() and move to search() or finditer()
    * start with a small pattern and build-up one step at a time


Flags:
======
    DOTALL         make the dot recognize all characters (usually it won't match a newline)
    MULTILINE      make ^ and $ match line beginnings and endings instead of string beginnings and endings                                                           
    IGNORECASE     make A-Z and a-z synonymous
'''
