# Queues
**Definition:** Elements within this abstract data type are ordered by a specified principle. An enqueue method adds an element to the back of the queue, while a dequeue method removes an element from the front of the queue. 

We'll cover the following:
* [1. FIFO](#fifo)
* [2. Deque](#deque)
* [2. Priority Queue](#priority-queue)

<br/>

## FIFO
The traditional queue policy is first in, first out (FIFO), just like a line for a service. Elements which are added to the queue earlier on are accessible sooner than elements added to the queue later on. 

### When to Use:
* Need to maintain order
* Packet transmission
* Providing a service in which clients are all valued equally

### Time Complexity:

| |Average|Worst|
|:---|:---|:---|
|**Access**|θ(n)|O(n)|
|**Search**|θ(n)|O(n)|
|**Insertion**|θ(1)|O(1)|
|**Deletion**|θ(1)|O(1)|

<br/>

## Deque
Elements can be inserted and removed from both the front and back of this type of queue. 

### When to Use:
* Need access to old and new elements
* Providing a service that is likely to require clients to return 
  * A fast food cashier serves a customer their order but forgets to include ketchup packets 
    * The customer is allowed to cut the line to get ketchup packets.

### Time Complexity:

| |Average|Worst|
|:---|:---|:---|
|**Access**|θ(n)|O(n)|
|**Search**|θ(n)|O(n)|
|**Insertion**|θ(1)|O(1)|
|**Deletion**|θ(1)|O(1)|

<br/>

## Priority Queue
Similar to a standard FIFO queue, except elements are assigned priorities, and these priorities determine the element's position in the queue. A priority queue is typically implemented with a min or max heap.

### When to Use:
* Event-driven scheduling
* Data compression 
* Graphing algorithms (Dijkstra, Prim)
* Bandwidth management

### Time Complexity:

| |Average|Worst|
|:---|:---|:---|
|**Access**|θ(1)|O(1)|
|**Search**|θ(n)|O(n)|
|**Insertion**|θ(nlog(n))|O(nlog(n))|
|**Deletion**|θ(nlog(n))|O(nlog(n))|
