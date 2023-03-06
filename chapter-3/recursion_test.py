
def has_key(data):
    for item in data:

        if type(item) is list and has_key(item):
            return True

        if type(item) is str and item == 'key':
            return True
        
    # return false if you've iterated over every item
    return False

data = [
    [ [ 'xxx', [ 'xxx', 'xxx', 'key' ] ] ],
    [ ['xxx', 'xxx'], ['yyy', 'zzz', 'xkey'] ]
]

print(has_key(data))