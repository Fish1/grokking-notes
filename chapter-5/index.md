# Notes

## What is a hash table?

Take a index, be it a number or string, and run it through a hash function.

The hash function will return a number, and with that number you put a value into that array index.

This means that we can get instant lookup time for any index string.

# Exercises

# 5.1

f(x) = 1

This hash function is consistant, but it is not a good hash function. It will always return the same index for any input.

# 5.2

f(x) = rand()

This hash function isn't consistant because it will return a different index for the same input.

# 5.3

f(x) = next_empty_slot()

This hash function isn't consistant because if you keep putting in the same input, it will increase.

# 5.4

f(x) = len(x)

This hash function is consistant, but it is not a good hash function. It will always return the same index for any input. And that index is out of bounds.

# 5.5

I would pick between the first letter of a name, and the prime number solution for a phone book. I would assume in a phone book there would be a fairly equal distribution of names.

# 5.6

I would use the length of the string as the hash because you know that each battery size has a different number of A's.

# 5.7

I would use the prime number solution.



