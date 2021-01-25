'''
------------------------------------------------------------------------------------------------
Union-find with specific canonical element. 
Add a method find() to the union-find data type so that find(i) returns the largest element in the connected component containing i. 
The operations, union(), connected(), and find() should all take logarithmic time or better.

For example, if one of the connected components is {1,2,6,9}, then the find() method should return 9 for each of the four elements in the connected components.
-------------------------------------------------------------------------------------------------

Modifying the find() method it is possible to insert a check for the maximum element of the branch.
When the maximum element is found it is associated with the root of that set in a separate list.

When it is asked to return the maximum element associated to an element p, it is necessary
to find the associated root of p, accessing the id[] array and then get the maximum from the hg[] array.

When two sets are joined the largest value between the two roots is assigned to the root having the lowest value in hg[].
'''



class WeightedUnion():
    def __init__(self, N):
        self.N = N
        self.id_list = [n for n in range(N)]
        self.sz_list = [1 for _ in range(N)]
        self.hg_list = [n for n in range(N)]
        self.count = N

    def find(self, p):
         #Here the maximum element is found and returned
         max_element = p
         while(self.id_list[p] != p):
             p = self.id_list[p]
             if p > max_element: max_element = p
         return p, max_element

    def find_max(self, p):
        return self.hg_list[self.id_list[p]]

    def union(self, p, q):
        root_p, p_max = self.find(p)
        root_q, q_max = self.find(q)
        if root_p == root_q: return False

        #checking the hg values for the root
        self.hg_list[root_p] = p_max 
        self.hg_list[root_q] = q_max
        #Here the largest hg is assigned to the lowest root
        if p_max >= q_max: self.hg_list[root_q] = p_max
        else: self.hg_list[root_p] = q_max

        if self.sz_list[root_p] < self.sz_list[root_q]:
            self.id_list[root_p] = root_q
            self.sz_list[root_q] += self.sz_list[root_p]
        else:
            self.id_list[root_q] = self.id_list[root_p]
            self.sz_list[root_p] += self.sz_list[root_q]                        
        self.count -= 1
        return True


def main():
    N = 10
    my_disjoint = WeightedUnion(N)

    my_disjoint.union(1,2)
    my_disjoint.union(6,2)
    my_disjoint.union(9,1)
    print("find(0) " + str(my_disjoint.find(0)))
    print("find(1) " + str(my_disjoint.find(1)))
    print("find(2) " + str(my_disjoint.find(2)))
    print("find(3) " + str(my_disjoint.find(3)))
    print("find(6) " + str(my_disjoint.find(6)))
    print("find(9) " + str(my_disjoint.find(9)))
    print("find_max(0) " + str(my_disjoint.find_max(0)))
    print("find_max(1) " + str(my_disjoint.find_max(1)))
    print("find_max(2) " + str(my_disjoint.find_max(2)))

if __name__ == "__main__":
    main()
