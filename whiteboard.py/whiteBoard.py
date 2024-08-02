# Given an array of integers.

# postive = .count(list)
# negative = sum(list)

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.
#.count, .sum(), return

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def solution(list):    
    positive = 0 #hopefully counting up to 10
    negative =  0
    for num in list:
        if num > 0:
            positive + 1
        elif num < 0:
            negative += list
    if len(list) == 0:
        return []
    return [positive, negative]
    