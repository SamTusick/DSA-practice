# DSA Dev Notes

## SORTING

### Bubble sort

- What does this solve / when would we use this? -
  It helps order a small array.
- Explain in english -
  Using a pointer variable traversing through the array decided weather the pointer item is greater than pointer + 1, if so swap, then continue, making multiple passes.
- Explain each step (Could be on Ipad) -
- Pros / Cons -
  Pros: Simple Cons: Slow and not efficent
- Big O -
  Time: O(n^2)
  Space: O(1)

### Selection sort

- What does this solve / when would we use this? -
  Ordering an array
- Explain in english -
  Start with 2 pointers at index 0, moving the second pointer to find the min value through the array, then swapping. After swapping move the first pointer up one than repeat.
- Explain each step (Could be on Ipad) -
- Pros / Cons -
  Pros: Simple Cons: Not efficent
- Big O -
  Time: O(n^2)
  Space: O(1)

### Insertion sort

- What does this solve / when would we use this? - Sorting data
- Explain in english - Compare one number with the number to the left repeatedly until no numbers on the left are smaller than it. Then swap.
- Explain each step (Could be on Ipad) -
- Pros / Cons - Pros: Simple Cons: Not most efficent
- Big O - Time - O(n^2) Space - O(1)

### Merge sort

- What does this solve / when would we use this? - Breaks down data and sorts it
- Explain in english - Break data in a array down to size 1, compare and merge 2 arrays, and repeat
- Explain each step (Could be on Ipad) -
- Pros / Cons - Very efficent
- Big O - Time- O(n log n) Space- O(n)

### Quick sort

- What does this solve / when would we use this? - Sort Data quickly
- Explain in english - Select a pivot index, move all data less than the pivot to the left and all data greater than to the right, then reselect pivot and repeat
- Explain each step (Could be on Ipad) -
- Pros / Cons - One of the most efficent sorting algorithms
- Big O - Time - O(n log n) Space - O(n^2)

## SEARCHING

## HASHING

## LINKED LISTS

## STACKS / QUEUES

## TREES
### Types:
   - Binary Tree - Each node has <= 2 childern  
   - Binary Search Tree (BST) - left < node < right  
   - Balanced Tree - Height is controlled  
   - Complete Tree - Filled left to right   
   - Full Tree - Each node has 0 or 2 childern   

### Traversal:
   - DFS(Depth First):  
       - Preorder(Root,left,right)
       - Inorder(left,root,right)
       - Postorder(left,right,root)
   - BFS(Level Order):  
       - Use a queue
## HEAPS

## GRAPHS
