# Notes

Greedy algorithms will pick the best local solution. This can work in some situations, but in more complex situations they might fail.

## NP-complete

To solve a set covering problem, you have to calculate every possible set. 

# Exercises

## 8.1

A greedy solution here would be to simply grab the smallest boxes first. 

## 8.2

You can either be greedy by picking the best places to go first, or the places that take the least time to visit.

It depends on which is better, if you can fit in lots of places that take very little time and its more worth it than a few really good places, then do that.

But if the really good places out weight the many quick places, then do that.

# 8.3

Quicksort is not a greedy algorithm, because it does not pick the best local solution, it picks the best global solution.

# 8.4

Breadth first search is not a greedy algorithm, it simply iterates through all the nodes in a tree, not picking the best local solution.

# 8.5

Dijkstra's algorithm is a greedy solution, because it will pick the lowest cost nodes to vist first.

# 8.6

A postman finding the shortest route between 20 homes is NP-complete. This is the travelling salesman problem.

# 8.7



# 8.8

This is NP-complete because you need to calculate the longest path between any two states.