def mergesort_desc(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left_side = mergesort_desc(arr[:mid])
    right_side = mergesort_desc(arr[mid:])
    return merge(left_side, right_side)

def merge(left_side, right_side):
    left_side_index = 0
    right_side_index = 0
    complete_merged = []

    while left_side_index < len(left_side) and right_side_index < len(right_side):
        if left_side[left_side_index] < right_side[right_side_index]:
            complete_merged.append(right_side[right_side_index])
            right_side_index += 1
        else:
            complete_merged.append(left_side[left_side_index])
            left_side_index += 1

    complete_merged += left_side[left_side_index:]
    complete_merged += right_side[right_side_index:]
    return complete_merged

def rearrange_digits(input_list):
    if len(input_list) == 0:
        return []
    if len(input_list) == 1:
        return input_list

    digits = mergesort_desc(input_list)

    odd, even = 0, 0
    for i, val in enumerate(digits):
        if i % 2 == 0:
            odd =  odd * 10 + val
        else:
            even = even * 10 + val
    return [odd, even]


# Edge cases
print('Edge Cases:')
print('Test 1:')
list_num = [1, 1, 1]
result = rearrange_digits(input_list=list_num)
if result == [11, 1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 2:')
list_num = [1]
result = rearrange_digits(input_list=list_num)
if result == [1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 3:')
list_num = []
result = rearrange_digits(input_list=list_num)
if result == []:
    print('Pass \n')
else:
    print("Fail \n")

# Normal cases
print('Normal Cases:')
print('Test 4:')
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(input_list=list_num)
if result == [531, 42]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 5:')
list_num = [4, 6, 2, 5, 9, 8]
result = rearrange_digits(input_list=list_num)
if result == [964,852]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 6:')
list_num = [1, 2, 3]
result = rearrange_digits(input_list=list_num)
if result == [31, 2]:
    print('Pass \n')
else:
    print("Fail \n")


