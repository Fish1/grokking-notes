# Notes

## What is an algorithm?

An algorithm is a set of instructions to accomplish a task.

## Simple Search vs Binary Search

A simple search will start at the first element and iterate over the entire data set to find a value.

A binary search will start in the middle, if the value it checks is too low it will goto the right half, other wise it will go to the left half.

Binary search takes logarithmic time, linear search takes linear time.

## Big O Notation

Big O notation is a way to describe the performance of an algorithm.

A simple linear search will take O(n) because it must iterate over n elemnts in the set. 

A binary search will take O(log n) because it can eliminate half of the data set with each iteration.



# Excercises

## 1.1

128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1

A sorted list of 128 names will take 7 steps, because you can divide 128 by 2, 7 times.

## 1.2

256 -> 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1

A sorted list of 256 names will take 8 steps, because you can divide 256 by 2, 8 times.

As the size of the data set doubles, the number of steps increases by 1 for O(log n) algorithms.

## 1.3

This will take O(log(n)) time because a phone book is sorted by name, so you can use a binary search.

## 1.4

A phone book isn't sorted by phone number, so you can't use a binary search. Meaning you must use a linear search, this will take O(n) time.

## 1.5

To read the number of every person in the book, you must linearly iterate over every person, O(n) time.

## 1.6

To read the number of all the A's in the book takes O(n) time because in the worst case the entire book is A's.
