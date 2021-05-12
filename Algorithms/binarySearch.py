# binary Search

# Time Complexity
# O(Log N)

# using bisect module

import bisect
li = [1, 3, 4, 4, 4, 6, 7]

# bisect_(right or left or none)(list, num, beg, end)

print ("The rightmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect(li, 4))

print ("The leftmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect_left(li, 4))

print ("The rightmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect_right(li, 4, 0, 4))


# Returns index of x in arr if present, else -1

#############
# Recursive #
#############
def bSearch(arr,l,r,x):
    if r>=l:
        mid = l+(r-l)//2

        if arr[mid] == x:
            return mid


        elif arr[mid] > x:

            return bSearch(arr, l, mid - 1, x)

        else:
            return bSearch(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 5

result = bSearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")


#############
# Iterative #
#############
def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2;

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")