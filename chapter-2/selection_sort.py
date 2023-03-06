def find_largest(data):
    max = data[0]
    for guess in data:
        if guess > max:
            max = guess
    return max

def selection_sort(data):
    new_data = []
    
    while len(data) != 0:
        largest = find_largest(data)
        data.remove(largest)
        new_data.append(largest)
    
    return new_data

arr = [5,2,3,5,6,3,12,4]

print("Unsorted", arr)

sorted = selection_sort(arr)

print("Sorted", sorted)