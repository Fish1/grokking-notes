
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left = []
    right = []

    for value in arr[1:]:
        if value <= arr[0]:
            left.append(value)
        else:
            right.append(value)

    return quick_sort(left) + [arr[0]] + quick_sort(right)


my_data = [33, 10, 15, 7, 1]

print(my_data)

my_data_sorted = quick_sort(my_data)

print(my_data_sorted)
