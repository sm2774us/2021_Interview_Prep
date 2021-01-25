# Linked Lists
**Definition:** A linear collection of nodes in which each node links to the next node.

We'll cover the following:
* [1. Singly Linked List](#singly-linked-list)
* [2. Doubly Linked List](#doubly-linked-list)

<br/>

## Singly Linked List
Each node has a single pointer to the next node.

### When to Use:
* Need constant time insertion or deletion 
  * Only at head (front of list) 
  * Inserting elements is easier in singly linked list that in doubly linked list
* Unknown number of elements
* No need for random access
* Need linked list and memory is a concern
  * Requires less memory than doubly linked list

### Time Complexity:

| |Average|Worst|
|:---|:---|:---|
|**Access**|θ(n)|O(n)|
|**Search**|θ(n)|O(n)|
|**Insertion**|θ(1)|O(1)|
|**Deletion**|θ(1)|O(1)|

<br/>

## Doubly Linked List
Each node has two pointers, one to the previous node and one to the next node.

### When to Use:
* Need constant time insertion or deletion
  * Only at head or tail (front or back of list)
  * Doubly linked list deletion is faster that singly linked list deletion, except when deleting the head
* Unknown number of elements
* No need for random access

### Time Complexity:

| |Average|Worst|
|:---|:---|:---|
|**Access**|θ(n)|O(n)|
|**Search**|θ(n)|O(n)|
|**Insertion**|θ(1)|O(1)|
|**Deletion**|θ(1)|O(1)|