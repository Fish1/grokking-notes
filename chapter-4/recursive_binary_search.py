
def binary_search(arr, search_value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]

        if guess == search_value:
            return mid
        elif guess < search_value:
            left = mid + 1
        else:
            right = mid - 1

    return None

def binary_search_r(arr, search_value):
    if len(arr) == 1:
        return 0

    mid = (len(arr) - 1) // 2

    if arr[mid] == search_value:
        return mid
    
    elif arr[mid] < search_value:
        return mid + binary_search_r(arr[mid:], search_value) + 1
    
    else:
        return mid - binary_search_r(arr[:mid], search_value) - 1
