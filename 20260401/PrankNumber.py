def fix_prank_number(arr):
    diffs = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    diff = max(set(diffs), key=diffs.count)
    
    result = []
    if arr[1] - arr[0] == diff:
        result.append(arr[0])
    else:
        result.append(arr[2] - diff - diff)
        
    for i in range(1, len(arr)):
        result.append(result[0] + i * diff)

    return result


# There are several key steps in completing the challenge.
# Firstly, calculate all the differences between every two consecutive items in the array.
# As described in the challenge, the correct difference should appear the most. Based on this, 
# it is easy to confirm the rule the whole array is built on.
# Then, check if the first two items in the array follow the rule. If they do, then it can be 
# confirmed that they are the correct items not the "Prank Numbers". If not, then there must be 
# a Prank Number in the first two items of the array. As there is only one Prank Number, it can
# be assured that the third item (and there must be a third item in the array, otherwise the 
# "Prank Number" setup does not make sense) should be a correct number.
# After this checkup, the correct first item of the array can be known. This number will then be
# assigned as the first item of result array.
# With the first item, the rule and the length of result array all known, the result array can be
# created and this is the array of input array without the Prank Number.
