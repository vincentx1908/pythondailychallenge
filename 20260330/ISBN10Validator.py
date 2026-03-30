def is_valid_isbn10(s):
    s = s.replace("-", "")

    if len(s) != 10:
        return False
    
    total = 0

    for i, ch in enumerate(s):
        if ch.isdigit():
            value = int(ch)
        elif ch == "X" and i == 9:
            value = 10
        else:
            return False
        total += (i + 1) * value

    return total % 11 == 0


# According to the challenge, these are the steps needed:
# 1. Eliminate the "-", by replacing them with ""
# 2. Do the calculation of number * its index, and sum all results together.
#   If the last character is "X", count as 10
# 3. Check if the total is divisible by 11.

# The key in the challenge is enumerate, where i is the index and ch is the character 
# at index i.
