# Assignment 2: Fractional Knapsack

## Important code

- `getMaxValue()` sorts items by value-to-weight ratio from highest to lowest.
- It takes complete items when possible and a fraction of the next item when capacity is insufficient.

## Concept used: Greedy algorithm

- A greedy algorithm makes the best choice available at the current step. It does not
  go back and change earlier choices.
- In this problem, the best choice is the item with the highest value for each unit
  of weight. The program can take part of an item, so the bag can be filled exactly.
- This strategy gives the maximum value for fractional knapsack because every unit
  of available capacity is assigned to the most valuable remaining item.

## Complexity of the program

- If there are `n` items, sorting takes `O(n log n)` time and checking the items
  takes `O(n)` time. Therefore, the total time is `O(n log n)`.
- The items and sorting support require `O(n)` extra space in this Java program.

## Complexity of the concept

- The greedy selection itself takes `O(n)` time when items are already sorted.
- Finding the correct order usually requires sorting, so the complete greedy
  solution is generally `O(n log n)` time and `O(n)` space.
