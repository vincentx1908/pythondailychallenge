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

# Although the code is only 1 line, it contains several layers of logics.
# 1. The input string s is split into words according to space (default method in .split(), so there is no need to write s.split(" "))
# 2. Each word is looped and its length is counted.
# 3. The length of each word is converted into string rather than integer.
# 4. All the lengths are joined together with spaces. Previously I used (+=) which as ChatGPT suggested is not efficient.
