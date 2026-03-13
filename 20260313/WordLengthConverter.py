# My solution to the challenge
def convert_words(s):
  # split the whole string into words  
  words = s.split(" ")
  # define a blank string to save the calculated word length  
  length = ""
  # loop through all the words in the string s and save their lengths into the string
    for word in words:
        length += f"{len(word)} "
  # Eliminate any space at the beginning/end of the length
    return length.strip()

# There are some small issues in the code
# 1. It is preferred to use s.split() rather than s.split(" ") as the latter will only split one space. The former way automatically splits words no matter how many spaces are there between two words
# 2. length += is less efficient so ideally it is recommended to use join to concatenate strings.

# A more pythonic way to the challenge:
def convert_words(s):
    return " ".join(str(len(word)) for word in s.split())
