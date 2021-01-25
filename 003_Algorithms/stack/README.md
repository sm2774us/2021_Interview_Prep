

A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))  is an [abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type). An abstract data type is different from a classical data structure. The data structures are concrete representations of data, and are the point of view of an implementer, not a user. The **data type** is defined by its behavior (semantics) from the point of view of a user of the data, specifically in terms of possible values, possible operations on data of this type, and the behavior of these operations. The stack is based on two principal operations: push and pop. **Push** adds an element to the collection and **pop** removes the most recently added element. For this reason stacks are considered LIFO (last in, first out).

It is important to make the implementation **generic**, meaning that the `class Stack` could contain any kind of object. In **C++** it can be done using templates. The class is based on a `vector` object. When declaring a new stack the template incorporates the type `Stack<int> my_int_stack` or `Sack<string> my_string_stack`, which is forwarded to the vector as `vector<int> vector_stack` or `vector<string> vector_stack`. In **Python** it can be possible to use an object `array`. The object `array` is like a list but it contains only objects of a specific type, which is specified at object creation time. The class can be imported using `from array import array`, and declared as `int_stack = array('i')` where the string `'i'` identifies the integer type, `'d'` is a double, and `'f'` is a float (other types are available). 


Implementation
--------------

1. **[Linked list](https://en.wikipedia.org/wiki/Linked_list)**: each element is defined by the data and a reference to the next element in the stack. The main advantage of a linked list for stack is that it does not require to adjust the dimension of the stack because there is not a size limit. However returning an item from a linked list takes linear time, because it is necessary to iterate on all the elements one after the other. This implementation can be selected if there is a stream of data coming and loosing some packets has an high cost. In Python the linked list is not represented by any built-in data structure. The Python list object is an array of references which store a reference to an object in each position of the list.

2. **Static array**: using an array is another way to implement a stack. The static implementation has a maximum capacity declared when the stack is created. It is necessary to monitor the size of the array because if the maximum capacity is exceeded then a [stack overflow](https://en.wikipedia.org/wiki/Stack_buffer_overflow) can occur.

3. **Resizing array**: in this implementation the size of the array is increased when a certain number of elements has been added. The resizing avoids the buffer overflow problem but can be quite slow because it requires to copy all the elements in a new array. A smart implementation will double the size of the array every time that the `resize()` method is called. In this way the next resize will happen less and less often. In particular, we can say that since the array double the `resize()` will be called with a logarithmic time. 

Methods
--------

- `push()`: it adds an element in the stack.
- `pop()`: it determines if two elements are in the same set.
- `isEmpty()`: returns True if the stack is empty.
- `resize()`: used only in the *resizing array* implementation.

Applications:
--------------

- Dijkstra's (or Shunting-yard) two stack algorithm for computing arithmetic operations [[link]](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)

- DO/UNDO operations are done accumulating everything in a stack.


Material
--------
- **Coursera Algorithms Part 1**: week 2
- **Algorithms**, Sedgewick and Wayne (2014): Chapter 1.3
