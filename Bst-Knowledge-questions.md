# Knowledge question for Assessment 4 Binary Search Tree

# Step 1 – Knowledge Question (20-50 words)
In your own words, describe what a Binary Search Tree (BST) is.
In addition, describe two important properties of a BST: depth and height. How are they different?

> A type of binary tree structure where nodes have their own unique keys that satisfies a specific ordering property.
> Also, its data structure is where the left subtree value is less than its parent value while the right subtree value is greater.
> Depth in Binary Search Tree is the total number of how deep does the tree goes. It starts at the root (first node) and measured on how deep you go
> Height in Binary Search Tree is the total number of how high the tree goes. It starts at the leaves of the tree and measured on how high the tree goes.

# Step 2 – Knowledge Question (50-80 words)
In your own words, describe how an algorithm to find an item in a Binary Search Tree works.

> The algorithm in the Binary Search Tree finds an item by comparing the item value towards the current node, it starts at the root
> then it continuously removes half of the remaining paths based on the tree's orders. As the left node is always smaller than the parent node and its right child is always bigger the algorithm can quickly
> find the location of the item. The search begins at the top most node then checks for a match or null and if the item value is smaller, then it will go to the left branch and if its bigger then, it will go to the right branch.
> This will happen again and again until it can a match or comes out null.

# Step 3 – Knowledge Question (20-60 words)
In your own words, describe what a balanced BST is.

> A balanced BST is where left and right subtrees height difference is at most one. For example, if the left subtree has a height of 4 and the right subtree has a height of 2 then it's unbalanced.