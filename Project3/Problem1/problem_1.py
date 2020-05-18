def helper(n,i,j):
    
    mid = (i + j) / 2;
    mul = mid * mid;
    if ((mul == n) or (abs(mul - n) < 0.00001)):
        return mid;
    elif (mul < n):
        return int(helper(n, mid, j));
    else:
        return int(helper(n, i, mid));  

def sqrt(number):
    if number==None:
        print("Invalid Input Type")
        return None
    i = 1
    find = False
    
    while find==False:
        if i*i==number:
            return i
        elif i*i>number:
            result = helper(number,i-1,i)
            return result
        i+=1
        
# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------

# Invalid Input Type
print("Pass" if (sqrt(None) is None) else "Fail")

# Edge Case Test
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")

# Regular Test
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# Large Number Test
print("Pass" if (9999 == sqrt(99999999)) else "Fail")


