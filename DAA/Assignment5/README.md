# Assignment 5: QuickSort Analysis

## Important code

- `partition()` places a pivot in its final position and separates smaller and larger values.
- The program compares deterministic QuickSort with randomized QuickSort and measures both execution times.

## Concept used: Divide and conquer

- QuickSort chooses a pivot and divides the array into values smaller than the pivot
  and values larger than it. The pivot is then already in its final position.
- The same process is applied recursively to the left and right parts. Small parts
  are automatically finished when their start and end positions meet.
- A good split makes the algorithm fast, while a very unbalanced split can be slow.
  Randomized QuickSort chooses the pivot randomly to reduce this risk on many inputs.

## Complexity of the program

- Deterministic QuickSort has average time `O(n log n)` and worst-case time `O(n^2)`.
  Its worst case can occur when the chosen last element gives very unbalanced parts.
- Randomized QuickSort has expected time `O(n log n)` and worst-case time `O(n^2)`.
  Both versions use `O(log n)` stack space on average and `O(n)` in the worst case.

## Complexity of the concept

- Divide and conquer is efficient when each division creates balanced subproblems.
  For QuickSort, balanced divisions give `O(n log n)` time.
- If divisions are repeatedly unbalanced, the recursion becomes `O(n^2)`. The
  algorithm sorts in place, so its extra space is usually `O(log n)` on average.
