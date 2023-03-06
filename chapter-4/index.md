# Notes

## Divide and Conquer

Divide and conquer is a strategy for problem solving. It is not an algorithm. The idea is to break a problem down into smaller bits. When the largert bit is solved, go to the smaller bit.

Algorithms such as quick sort use a divide and conquer strategy. The idea is to break the array down into two halves. Then execute the sort on each half. The two halves are then merged together.

## Average vs Worst Case

The average case is the average time it takes to solve a problem. The worst case is the longest time it takes to solve a problem. The worst case is the most important. The worst case is the time it takes to solve a problem when the input is the worst possible input.

But if two algorithms both have the same average case, and the constant runtimes are different, then one should consider the constant in the runtime.

Quicksort has a smaller constant than merge sort. So quicksort is generally faster than merge sort because quicksorts average case is O(n * log(n)) and merge sort is O(n * log(n)).

# Exercises

## 4.1

```python
def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])
```

## 4.2

```python
def count(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + count(arr[1:])
```

## 4.3

```python
def max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], max(arr[1:]))
```

## 4.5

O(n) time to print every element in an array.

## 4.6

O(n) time to double each element in an array.

## 4.7

O(1) time to double just the first element in an array.

## 4.8

O(n^2) time to create a multiplication table.