
def binary_search(data, value):
    left = 0
    right = len(my_array) - 1

    while left <= right:
        mid = (left + right) // 2
        value_at_mid = data[mid] 
        if value_at_mid == value:
            return mid
        elif value_at_mid > value:
            right = mid - 1
        elif value_at_mid < value:
            left = mid + 1
    
    return None

my_array = [1, 2, 3, 4, 6, 7, 8, 9, 10]

print(binary_search(my_array, 5))

print(binary_search(my_array, 11))

print(binary_search(my_array, 1))

print(binary_search(my_array, 0))

print(binary_search(my_array, 6))

print(binary_search(my_array, 4))