def add_punctuation(s):
    result = ""

    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == " " and s[i+1].isupper():
            result += "."
        result += s[i]
      
    return result + "."

# The code loops through the given string, checks if there is a space followed by a capital letter,
# if so, add a period  to the newly created result string and then add the letter after.
# the idea is to iterate through every and each character in the string rather than add period into the whole 
# string.

# Another method using regex:

import re

def add_punctuation(s):
    result = re.sub(r' (?=[A-Z])', '.', s)
    return result + "."
