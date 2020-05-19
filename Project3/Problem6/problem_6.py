def get_min_max(array):
    if len(array) == 0:
        return None

    maximum_value = - float("inf")
    minimum_value = float("inf")

    for i in array:
        
        if i > maximum_value:            
            maximum_value = i
            
        if i < minimum_value:            
            minimum_value = i

    return (minimum_value, maximum_value)

import random
# Edge cases
print('Edge Cases:')
# Case 1
l = [i for i in range(300, 301)]  # a list containing 300
random.shuffle(l)
print("Pass" if ((300, 300) == get_min_max(l)) else "Fail")

# Case 2
l = []  # an empty list
print("Pass" if (None == get_min_max(l)) else "Fail")

# Case 3
l = [i for i in range(-24, -1)]  # a list containing -24 - -2
random.shuffle(l)
print("Pass" if ((-24, -2) == get_min_max(l)) else "Fail")

# Normal cases
print('Normal Cases:')
# Case 4
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Case 5
l = [i for i in range(-12, 25)]  # a list containing -12 - 24
random.shuffle(l)
print("Pass" if ((-12, 24) == get_min_max(l)) else "Fail")
print('\n')

