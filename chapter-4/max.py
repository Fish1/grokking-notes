
def max(arr):
    if len(arr) == 1:
        return arr[0]

    smaller_max = max(arr[1:])

    if arr[0] > smaller_max:
        return arr[0]
    else:
        return smaller_max
    

print(max([1,2,3,4,5]))
print(max([1,2,30,4,5]))
print(max([1,2,3,40,5]))
print(max([1,200,3,4,5]))
