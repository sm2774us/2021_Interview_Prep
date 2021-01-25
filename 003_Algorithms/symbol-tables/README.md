
A [Symbol Table](https://en.wikipedia.org/wiki/Symbol_table) data structure associates a key to a value. They are also known as associative arrays, **maps**, or **dictionaries**. The client can insert key-value pair in the table and can later return the value using the key. 
It is not possible to have **duplicated keys** because when a new element associated with an existing key is added, the old key is kept and the associated value is overwritten.

Implementation
--------------

1. **Linked list**: The keys are stored in a sequence of linked nodes. To find the value associated to a key it is necessary to scan the list and comparing the input key with the current key (sequential search). The same mechanism is used for both `get()` and `put()`. In particular in the `put()` method it is necessary to scan the array looking for the key, if the key is found then it can be returned otherwise the input key is added at the head of the linked list referring to the next element. The main problem of this approach is the time complexity, that is O(N) for both `get()` and `put()`.

2. **Ordered array:** using and ordered array for the keys to be stored, it is possible to use *binary search* for `get()`, reducing the time complexity to O(log N). Using an ordered array makes also extremelly fast to return the maximum and minimum keys (operations often used). Moreover it makes possible to manage particular keys, such as times and dates. The same problem remains for the method `put()` since to add a new element it is necessary to find the insertion point (it can be done with binary search) and then shift of one position all the elements that are greater than the key. In the worst case it will be necessary to shift all the keys (time complexity: O(N)). Those problems are solved using [binary search trees](https://en.wikipedia.org/wiki/Binary_search_tree), which are introduced in the next lesson.


Methods
--------

`put(key, value)`: insert a new pair of key-value. It must not be allowed to associate a `None` (python) value.

`get(key)`: return the value associated with the key. If the key does not exist it is possible to return `None`.

`remove(key)`: remove the key and the associated value.

`rank(key, lo, hi)`: (ordered array) the method is used in ordered array to search for a specific key using binary search. If the key is in the array it returns the index.

Applications
------------

1. Dictionaries: which is the application that also gives the name to the data structure (key=word, value=definition)
2. Account management: it can be used to process transactions (key=account id, value=transaction detail)
3. Web search: find relevant pages based on keywords (key=keyword, value=web pages)

Quiz
-----




Material
--------
- **Coursera Algorithms Part 1**: week 4
- **Algorithms**, Sedgewick and Wayne (2014): Chapter 3.1 "Symbol Tables"
