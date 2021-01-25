

A [queue](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))  is an [abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type) where the entities in the collection are kept in order and the principle (or only) operations on the collection are the addition of entities to the rear terminal position, known as enqueue, and removal of entities from the front terminal position, known as dequeue. This makes the queue a First-In-First-Out (FIFO) data structure. 

Implementation
--------------

1. **[Linked list](https://en.wikipedia.org/wiki/Linked_list)**: each element is defined by the data and a reference to the next element in the queue. It is necessary to have two additional values which store the index of the head and tail. The head and tail are necessary and when missing can increase the time of queue and/or dequeue operations. For instance, if the tail is missing when adding and element (queue) will be necessary to access all the elements in order to arrive at the last one (it takes linear time) and then add the reference to the queued new element. If the reference to the tail is present it is only necessary to access to this reference and then add the queued element (it takes constant time).

2. **Resizing array:** fixed length arrays are limited in capacity, but it is not true that items need to be copied towards the head of the queue. When the maximum capacity of the array is exceded it is possible to create a circular array. The simple trick of turning the array into a closed circle and letting the head and tail drift around endlessly in that circle makes it unnecessary to ever move items stored in the array. If *N* is the size of the array, then computing indices modulo *N* will turn the array into a circle. 

Methods
--------

- `enqueue()`: it adds an element in the queue tail.
- `dequeue()`: it pop an element from the head.
- `isEmpty()`: returns True if the stack is empty.


Material
--------
- **Coursera Algorithms Part 1**: week 2
- **Algorithms**, Sedgewick and Wayne (2014): Chapter 1.3
