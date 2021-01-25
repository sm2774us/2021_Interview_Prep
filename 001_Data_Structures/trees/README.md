# Trees
**Definition:** A hierarchical structure of parent-child relationships between nodes. Each parent will be one level higher on the structure than its children, respectively. Trees are non-cyclic but may be linear. 

We'll cover the following:
* [1. Binary Search Tree](#binary-search-tree-bst)
* [2. AVL Tree](#adelson-velskii-and-landis-avl-tree)
* [3. Red Black Tree](#red-black-tree)

<br/>

## Binary Search Tree (BST)
This type of tree may have one, two, or no children. A child is either to the left or right of a parent node. A parent's left child must have a value less than its own value, and a parent's right child must have a value greater than its own value. It is common for repeated nodes to be disallowed; however, in the case of a BST which allows repeated nodes, either the left child condition or the right child condition can be modified to handle equal values. 

### When to Use:
* Goal of average case of log(n) for all operations
* Need memory efficient solution to storing data
* Expression evaluation
* Data compression

### Time Complexity:
| |Average|Worst|
|:---|:---|:---|
|**Access**|θ(log(n))|O(n)|
|**Search**|θ(log(n))|O(n)|
|**Insertion**|θ(log(n))|O(n)|
|**Deletion**|θ(log(n))|O(n)|

<br/>

## Adelson-Velskii and Landis (AVL) Tree
Self-balancing BST in which the difference in height between left and right subtrees cannot exceed one for all nodes. If a node is inserted or deleted such that the height condition is violated, an AVL tree will reorder itself to meet its height conditions and standard BST conditions. 

### When to Use:
* Lookup time is priority
  * Fastest of the trees in terms of lookup time
* Not concerned with insertion and deletion times
  * Slow insertions and deletions due to strict height requirements
  * Requires rebalancing often

### Time Complexity:
| |Average|Worst|
|:---|:---|:---|
|**Access**|θ(log(n))|O(log(n))|
|**Search**|θ(log(n))|O(log(n))|
|**Insertion**|θ(log(n))|O(log(n))|
|**Deletion**|θ(log(n))|O(log(n))|

<br/>

## Red-Black Tree
Self balancing BST with each node being assigned a color, either red or black. It is similar to an AVL tree; however, balancing is not as rigid (the farthest leaf from the root can be up to twice as far as the nearest leaf from the root) and reorganizing the tree is done in a more efficient manner. The following are the requirements for a red-black tree:

1. Nodes are either red or black
2. Root node is black
3. Leaves are black
4. Red nodes have black children
5. The number of black nodes between any node and its leaves is the same 

### When to Use:
* Guaranteed O(log(n)) for all operations
* Balance between fast look ups and efficient insertions and deletions
 
### Time Complexity: 
| |Average|Worst|
|:---|:---|:---|
|**Access**|θ(log(n))|O(log(n))|
|**Search**|θ(log(n))|O(log(n))|
|**Insertion**|θ(log(n))|O(log(n))|
|**Deletion**|θ(log(n))|O(log(n))|
