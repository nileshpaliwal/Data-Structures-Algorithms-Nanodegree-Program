def sort_012_method_1(input_list): 
    pivot, start_point, mid_point, end_point = 1, 0, 0, len(input_list) - 1
    while mid_point <= end_point:
        if input_list[mid_point] < pivot:
            swap(input_list, start_point, mid_point)
            start_point, mid_point = start_point + 1, mid_point + 1
        elif input_list[mid_point] > pivot:
            swap(input_list, end_point, mid_point)
            end_point -= 1
        else:
            mid_point += 1
    return input_list


def swap(input_list, start_point, end_point):
    input_list[start_point], input_list[end_point] = input_list[end_point], input_list[start_point]

def test_function(test_case):
    sorted_array = sort_012_method_1(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
        

# Edge cases
print('Edge Cases:')
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])
# Normal cases
print('Normal Cases:')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('\n')

