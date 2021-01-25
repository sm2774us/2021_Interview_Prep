
The [hash function](https://en.wikipedia.org/wiki/Hash_function) is any function that can be used to map data of arbitrary size to data of fixed size. Hash functions are used in hash tables to solve the problem of storing a large number of values. There are two main problems solved by the hash function. The **first problem** is **space** constraint, that emerges when we want to store a large number of values. If we do not have any space limit we do not need an has function and we can simply store a value associating the key to the index of an array. The **second problem** is search **time**. The hash allows searching with complexity O(1), whereas a linked list is O(N). The only problem with hash functions are **collisions** which can happen when different keys are assigned to the same index in the array. This problem is solved in two ways: separate chaining, linear probing.

**Modular hashing**: it is used a prime number M to divide (and take the reminder) the hash value returned as an integer. In this way the large integer retuned with the hash is compressed in a well defined space that goes from 0 to M-1. In probabilistic terms is like throwing balls uniformly at random into M bins. Sometimes the hash can return a negative values, for this reason is necessary to take the absolute value of the hash before taking the reminder through M. Thinking in probability terms (with combinatorial analysis) tells us that we expected to have two balls in the same bin after *sqrt(pi M / 2)* (birthday problem), and that every bin has >= 1 balls after *M ln M* tosses (coupon collector). It is important to notice that returning the hash function of a string takes time proportional to the length of the string because hashing involves performing arithmetic operations on each character of the string. It may be necessary to mask the negative bit of the hash instead of using a simple `abs()` method because there is a bug in one of a billion cases where a negative value is returned also after applying the absolute.

Implementation
---------------

1. **separate chaining**: this implementation has been invented in the 1953 by Luhn at IBM. It consists in adding a linked list in any position of the array. In this way if there are collisions the colliding keys are chained in the same position. When looking for a specific key we access the location and then we do a linear search on the linked list. Under the uniform hashing assumption (the hash uniformly spread the integers across the bins). We have  cost of N/M, where N is the sequential cost required to search N values in a linked list, and M is the number of array elements mapped through the has function. For instance, if we have N=10^4 that is larger than the available number of bins (let's suppose M=10^3) the cost for searching a key will be only 10 (10^4 / 10^3). In particular the distribution of list size is binomial. The choice of M is important, and in general it is necessary to choose a value that is not too small (otherwise the linked list associated to the bin is large) and not too large (otherwise there are a lot of empty bins). The ideal size generally chosen is M=N/5. The *main advantage* of the separate chaining implementation is constant time in case of a search miss, due to the fact that empty bins do not have any linked list associated.

2. **linear probing**: the idea behind linear probing is to have an array where the number of bins M is larger that the number of keys N. When a value is added and it collides, then it is possible to look at position *i+1* and if it is free store the key there. Every time there is a collision we look for higher locations and we insert the key at the first available. When the end of the array is reached it is necessary to restart from the first position, and always look for a free place. When we search for a key we can use the same idea. We start from the index pointed by the hash and then we start a linear search increasing *i*. We get a search miss if an empty place is found along the path, meaning that the key was not stored before that point. Also in this case the right choice of M is important. If M is small then search time for an item blows up (because the seach it can take a long time), whereas if it is too large then there are too many empty positions and waste of memory. The array dimension must be monitored, and when more than half of it has been filled it is necessary to increase the dimension to make room for new keys. A particular note is needed when the `remove()` method is called. In this case it is necessary to find the key, remove it and then reinsert all the keys after that one. If the size of M is correct then not many keys have to be reinsert. An alternative is to flag the key to delete, reuse it again at the next insert and skip it during a search.

Methods
--------

`put(key, value)`: insert a new pair of key-value. It must not be allowed to associate a `None` (python) value.

`get(key)`: return the value associated with the key. If the key does not exist it is possible to return `None`.

`remove(key)`: remove the key and the associated value.

`hash(key)`: internal function that returns the integer associated with the key value.

`equals(key, key)`: used to search for a key into the array

Applications
------------

1. This is not a real application but a vulnerability. If an attacker discover the hash function used, then it can send a range of numbers that always generate the same key, leading to a pile of keys allocated in the same array bin. For instance in Linux 2.4 the problem arose when saving files with some specific names.

Quiz
-----




Material
--------
- **Coursera Algorithms Part 1**
- **Algorithms**, Sedgewick and Wayne (2014): Chapter 3.4 "Hash tables"
