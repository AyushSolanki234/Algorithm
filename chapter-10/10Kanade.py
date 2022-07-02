def maxArraySum(array, n):
    max_till_now = array[0]
    max_ending = 0

    for i in range(0, n):
        max_ending = max_ending + array[i]
        if max_ending < 0:
            max_ending = 0


        elif (max_till_now < max_ending):
            max_till_now = max_ending

    return max_till_now


array = [-1, -4, 4, -2, -2, 5, -3]
print("Max Sub-Array Sum is: ", maxArraySum(array, len(array)))
