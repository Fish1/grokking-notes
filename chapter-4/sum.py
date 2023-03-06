
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def sum_r(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    x = arr.pop()
    return x + sum_r(arr)

print(sum([1,2,3,4]))
print(sum_r([1,2,3,4]))