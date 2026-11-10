# Assignment 3: Huffman Coding

## Important code

- `PriorityQueue` always removes the two nodes with the smallest frequencies.
- `generateCodes()` walks left as `0` and right as `1` to create a binary code for every character.

## Concept used: Greedy tree construction

- Huffman coding is a lossless compression method, so the original data can be
  recovered exactly after decoding.
- The two least frequent nodes are joined repeatedly. This builds a binary tree where
  frequent characters usually get short codes and rare characters get longer codes.
- A character's code is the path from the root to its leaf: left means `0` and right
  means `1`. No code is the prefix of another code, so decoding is unambiguous.

## Complexity of the program

- For `n` different characters, repeatedly removing and adding heap nodes takes
  `O(n log n)` time. Generating the codes takes `O(n)` time.
- The priority queue, tree, and output string use `O(n)` space.

## Complexity of the concept

- Huffman tree construction is `O(n log n)` time when a priority queue is used.
- The tree and generated code table require `O(n)` space. The final compressed
  message size depends on the characters' frequencies and code lengths.
