def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0

    last = len(arr) - 1

    completed = False

    if len(arr) > 0:

        while first <= last and not completed:
            middle = (first + last) // 2

            if arr[middle] == target:
                completed = True
                return middle

            elif target < arr[middle]:
                    last = middle - 1

            elif target > arr[middle]:
                    first = middle + 1

            else:
                completed = True
                return  -1
    else:
        return -1
