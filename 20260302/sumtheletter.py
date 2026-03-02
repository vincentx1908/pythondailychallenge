## This challenge is easy comparing some previous ones
## I finished it with the following solution within a minute
def sum_letters(s):
    words = "abcdefghijklmnopqrstuvwxyz"
    value = 0
    for ch in s:
        if ch.isalpha():
            value += (words.index(ch.lower()) + 1)
    return value

## However when asked ChatGPT, a better evolved solution was given without manually typing in the alphabet
## Ord function was used. It gets the ordinal value of a character, from ASCII. 

# 'a' → 97
# 'b' → 98
# 'c' → 99
# ...
# 'z' → 122

def sum_letters(s):
    total = 0
    for ch in s:
        if ch.isalpha():
            total += ord(ch.lower()) - ord('a') + 1
    return total

## Even a one line solution although not as readable as the above one

def sum_letters(s):
    return sum(ord(ch.lower()) - ord('a') + 1 for ch in s if ch.isalpha())
