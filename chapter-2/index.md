# Notes

## Arrays vs Linked lists

Arrays are stored in contiguous memory, if you ever need more space you must request an entirely new array, and copy over all your data.

Linked lists are nodes that point to other nodes in memory. If you want to add to a linked list, simply request one spot in memory and store a pointer to it.

Generally to find data inside a linked list, you must iterate from the start or end, and search for the element you want. You cannot use direct memory access like you can with arrays.

## Insertions

Insertions into an array are expensive, because you must copy over all the data after the insertion point.

Insertions into a linked list are cheap, because you only need to change the pointer of the middle node to point to your new node.

# Deletions

Deletions from an array are expensive, because you must copy over all the data after the deletion point.

Deletions from a linked list are cheap, because you only need to change the pointer of the middle node to point to the node after your deleted node.

# Excercises

# 2.1

I would use a linked list, beacuse you do not know how many items you want to add to your expense list.

# 2.2

For a list of incoming orders, I would use a linked list. We do not know how many orders we need to store. So having a dynamically linked list can handle as many orders as we need. The chef will just need to take the first order, and the waiter simply adds to the end. Both of these operations are O(1) time.

# 2.3

If quick lookup is important, then I would use an array and take advantage of a binary search. But we might also consider how many people are signing up for facebook, if lots of users are signing up, we need to copy over the users array a lot. It might be better to use a linked list, because we can add to the end of the list in O(1) time.

# 2.4

As stated in the previous answer, it will take O(n) time to append a new user. Because we must copy over the entire array to a new array with one more spot.

# 2.5

This kinda hybrid data structure is almost like a hash map. But it is not because the hash is simply alphabetical. In theory all the users could start with an A, resulting in every user going into the same bucket. This would result in the data structure simply being a linked list. So we couldn't use a binary search anyways.