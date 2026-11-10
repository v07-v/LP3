# Assignment 1: Fibonacci Step Count

## Important code

- `CombinedFibonacci.py` runs both methods in one program and prints their sequences
  and step counts side by side for comparison.
- `Assign1.py` builds Fibonacci numbers iteratively using two running terms. It also increments `stepCount` to show the number of counted operations.
- `Assign1_1.py` uses `calculateFibonacci()` recursively. The counter records each function call, showing how recursive work grows.

## Concept used: Recurrence and complexity analysis

- The Fibonacci sequence is defined by `F(n) = F(n-1) + F(n-2)`. Each new number
  depends on the two numbers before it.
- The iterative program stores only the previous two values, so it uses little memory
  and runs efficiently. The recursive program creates many repeated function calls.
- The step counter gives a simple way to observe this difference. It helps explain
  why the recursive method becomes slow as the number of terms increases.

## Complexity of the programs

- **Iterative program:** Time is `O(n)` because it prints and calculates `n` terms.
  Space is `O(1)` because it stores only a few Fibonacci values.
- **Recursive program:** Time is `O(2^n)` because the same Fibonacci values are
  calculated repeatedly. Space is `O(n)` for the recursive call stack.

## Complexity of the concept

- The iterative Fibonacci idea can be implemented in `O(n)` time and `O(1)` space.
- The direct recursive recurrence uses `O(2^n)` time and `O(n)` stack space unless
  memoization is added.
