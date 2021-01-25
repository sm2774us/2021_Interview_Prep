# Hash Tables
**Definition:** An associative structure with mappings between keys and values. A hash function is used on a key to compute an index for a given value. Furthermore, once a hash table has been filled passed a predefined load factor, which is a ratio of the number of filled positions to the number of total positions, the hash table is resized. Ideally, hash tables have the following properties:

* Size of hash table is prime at initialization and upon resizing
* Values are evenly distributed
* Hash function minimizes the number of collisions (keys hashing to same index)  

In the event of a collision, either open addressing or separate chaining can be used to resolve the collision. 

We'll cover the following:
* [1. Open Addressing](#open-addressing)
* [2. Separate Chaining](#separate-chaining)


<br/>

## Open Addressing
Resolves collisions by probing alternative locations for availability. There are three main types of probing: 

1. Linear probing
2. Quadratic probing
3. Double hashing

In **linear probing** the interval of the probe is fixed at a constant value, so if the constant was set to 1 and a collision occurred at position i, then the probe would follow the sequence i+1, i+2, i+3, ..., i+n, until an open position was found.

In **quadratic probing** the interval of the probe is incremented linearly and then squared, so if the constant was set to 1 and a collision occurred at position i, then the probe would follow the sequence i+1<sup>2</sup>, i+2<sup>2</sup>, i+3<sup>2</sup>, ..., i+n<sup>2</sup>, until an open position was found.

In **double hashing** the interval of the probe is fixed at a constant value and run through a second hash function. The resulting value is added to the initial index in which the collision occurred, so if the constant was set to 1 and there is a second hash function H<sub>2</sub>(x), then the probe would follow the sequence i+H<sub>2</sub>(1), i+H<sub>2</sub>(2), i+H<sub>2</sub>(3), ..., i+H<sub>2</sub>(n), until an open position was found.  

### When to Use:
* Fast look ups
  * Typically faster than separate chaining
* Small load factor
  * Outperforms separate chaining when load factor is small
* Ordering is not relevant

### Time Complexity:
| |Average|Worst|
|:---|:---|:---|
|**Access**|N/A|N/A|
|**Search**|θ(1)|O(n)|
|**Insertion**|θ(1)|O(n)|
|**Deletion**|θ(1)|O(n)|

<br/>

## Separate Chaining
Each position in the hash table contains a bucket of some sort (linked list, binary tree). Whenever a collision occurs, the colliding value is inserted into the corresponding bucket. If multiple values are contained in a bucket and the index for that bucket is called, then the bucket's find method must be invoked. Typically, only one value should be associated with each bucket, and three values at the upper limit; otherwise, the average case for lookup times will approach θ(n). 

### When to Use:
* Fast look ups
* Large load factor
  * Outperforms open addressing as load factor increases
* Ordering is not relevant
* Need simplicity
  * Easier to implement than open addressing hash tables

### Time Complexity:
| |Average|Worst|
|:---|:---|:---|
|**Access**|N/A|N/A|
|**Search**|θ(1)|O(n)|
|**Insertion**|θ(1)|O(n)|
|**Deletion**|θ(1)|O(n)|