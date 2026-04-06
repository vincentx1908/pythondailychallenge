def capitalize_fibonacci(s):
    fibo = [0, 1]
    s = s.lower()
    while fibo[-1] < len(s):
        fibo.append(fibo[-1] + fibo[-2])
    
    fibo_set= set(fibo)

    result = ""
    for i in range(len(s)):
        if s[i].isalpha() and i in fibo_set:
            result += s[i].upper()
        else:
            result += s[i]
        
    return result


# The core of solving this challenge contains the following steps:
# 1. Create a long enough Fibonacci list. "Long enough" means the biggest number
# (the last number) of the Fibonacci list is greater than the length of the input 
# string, so that it is able to check whether the index of a character is a Fibonacci 
# number.
# 2. Check the index of every character in the string. If it is a Fibonacci number,
# shift the character to uppercase, otherwise leave as lowercase.
# 3. Append all characters into a new result string and return it.
