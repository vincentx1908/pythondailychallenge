def convert_words(s):
    return " ".join(str(len(word)) for word in s.split())

# Although the code is only 1 line, it contains several layers of logics.
# 1. The input string s is split into words according to space (default method in .split(), so there is no need to write s.split(" "))
# 2. Each word is looped and its length is counted.
# 3. The length of each word is converted into string rather than integer.
# 4. All the lengths are joined together with spaces. Previously I used (+=) which as ChatGPT suggested is not efficient.
