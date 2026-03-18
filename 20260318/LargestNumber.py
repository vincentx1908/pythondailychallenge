import re
def largest_number(s):
    numbers = re.findall(r"-?\d+(?:\.\d+)?", s)
    numbers = [float(n) for n in numbers]
    return max(numbers)


# When I saw this challenge I immediately think of a way to do it with regex.
# First get all the numbers into the numbers list using regex to eliminate the symbols and separate the numbers
# with symbols.
# Then convert all the numbers in the list to float, getting ready to compare.
# Last step is just to find the max number in the numbers list and return.

# ChatGPT provided another method without using regex.

def largest_number(s):
    for sep in ",!?:;":
        s = s.replace(sep, " ")
    numbers = s.split()
    numbers = [float(n) for n in numbers]
    return max(numbers)

# This method is actually easy to understand and easy to write as errors might occour when creating regex rules.
# For the first several tries I ended up forgetting to consider negative numbers and float numbers.
# This method actually convert all symbols into spaces at first.
# After that it only requires simple split of all the numbers, without considering what the number is thus no need to 
# create rules for particular kinds of numbers, making it less prone to make mistakes.
# Similarly it then convert all numbers into float.
# And lastly return the max number in the numbers array.
