
def count_down(start):
    print(start)
    if start <= 0: # base case of start <= 0
        return
    count_down(start - 1) # recursive case

count_down(5)