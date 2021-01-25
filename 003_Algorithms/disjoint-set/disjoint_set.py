
#We shall consider three different implementations, all based on
#using the site-indexed id[] array, to determine whether two sites are in the same connected component.
#The integer inside the array id[] represent the component. For instance if nine elements are grouped in
#three components then inside the array id[] we can have something like: id[0,3,3,0,0,8,8,0,3]
#The numbers 0,3,8 represent the label associated to each component.
#
# 1. Quick-find
# 2. Quick-union
# 3- Weighted-union


class QuickFind():
    '''
    In this implementation of the disjoint-set data structure the find() 
    operation is quick because it only needs to access the elements of a list.
    The problem with this implementation is that union() needs to scan
    through the whole id[] array for each input pair in order to apply the 
    union operator when needed. This operation must be done in all the cases.
    '''

    def __init__(self, N):
        #At the beginning the number of components is equal to the number of elements.
        self.id_list = [n for n in range(N)]
        self.count = N

    def find(self, p):
         #The find operation is really fast.
         return self.id[p]

    def union(self, p, q):
        '''
        This operation can be interpreted as:
        I put p and all the elements that are in the same component of p, 
        into the component of q.
        For instance: union(3,8) means that the
        element 3 (and all the other in the same component) 
        must be added into the component of 8.
        '''
        p_id = self.find(p)
        q_id = self.find(q)

        #we first check whether they are already in the same component, 
        #in which case there is nothing to do.
        if p_id == q_id return False

        #Here we are faced with the situation that all of the self.id_list entries
        #corresponding to sites in the same component as p have one value and 
        #all of the self.id_list entries corresponding to sites in the same component as q have another
        #value. To combine the two components into one, we have to make all of the id[] entries 
        #corresponding to both sets of sites the same value.
        for i, _id in enumerate(self.id_list):
            if _id == p_id: _id = q_id
        self.count -= 1
        return True


class QuickUnion():
    '''
    In this implementation of the disjoint-set data structure we focus on speeding
    up the union() operation. 

    To implement find(), we start at the given site, follow its link to another
    site, follow that site’s link to yet another site, and so forth, following
    links until reaching a root, a site that has a link to itself (which is guaran-
    teed to happen). Two sites are in the same component if and only if this process
    leads them to the same root.

    The quick-union algorithm would seem to be faster than the quick-find algorithm, 
    because it does not have to go through the entire array for each input pair;
    However in the worst case scenario it will have to iterate through the entire
    array before finding a root node, for instance in a structure like:
    1>2>3>4>5>6>7>8 when the function union(7,8) is called it has to iterate back
    to the root 1 and scan the entire array leading to complexity O(N^2).

    You can regard quick-union as an improvement over quick-find because it
    removes quick-find’s main liability (that union() always takes linear time). 
    This difference certainly represents an improvement for typical data, but 
    quick-union still has the liability that we cannot guarantee it to be 
    substantially faster than quick-find in every case
    '''

    def __init__(self, N):
        self.N = N
        self.id_list = [n for n in range(N)]
        self.count = N

    def find(self, p):
         #The find operation is slower than the previous implementation.
         while(self.id[p] != p):
             p = self.id[p]
         return p

    def union(self, p, q):
        '''
        The union operation is fast,
        it only needs to call the find() method and get the root
        nodes of both the elements, and use this information to
        decide if the elements can be joined (if they are in
        different sets) or not (they already are in the same set).
        '''
        root_p = self.find(p)
        root_q = self.find(q)
        #Element already in the same set
        if root_p == root_q: return False
        #Elements in different sets they point to the same node.
        self.id_list[root_p] = root_q
        self.count -= 1
        return True


class WeightedUnion():
    '''
    In this implementation of the disjoint-set data structure we focus on optimizing
    the union operation when two trees are joined in a common set. Merging a short tree
    with the large one, it is possible to keep contained the depth of the resulting tree.
    This simple trick allows reducing the complexity to O(log N)

    This improvement requires a new list in order to store the size of the set.
    '''

    def __init__(self, N):
        self.N = N
        self.id_list = [n for n in range(N)]
        self.sz_list = [1 for _ in range(N)] #A new list is required to store the size of the set
        self.count = N

    def find(self, p):
         #The find operation equal to the one in QuickUnion implementation.
         while(self.id[p] != p):
             p = self.id[p]
         return p

    def union(self, p, q):
        '''
        In this implementation of union we have to add a check on the size of the trees.
        The shorter tree is linked to the longest, using the second as root.
        '''
        root_p = self.find(p)
        root_q = self.find(q)
        #Element already in the same set
        if root_p == root_q: return False
        #Elements in different sets
        if self.sz[root_p] < self.sz(root_q):
            self.id_list[root_p] = root_q
            self.sz[root_q] += self.sz[root_p]
        else:
            self.id_list[root_q] = self.id_list[root_p]
            self.sz[root_p] += self.sz[root_q]                        
        self.count -= 1
        return True

