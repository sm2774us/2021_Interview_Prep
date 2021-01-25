
'''
-----------------------------------------------------------------------------------------------------------
Successor with delete. 
Given a set of n integers S={0,1,...,n-1} and a sequence of requests of the following form:

1. Remove x from S
2. Find the successor of x: the smallest y in S such that y>=x.

design a data type so that all operations (except construction) take logarithmic time or better in the worst case.
-----------------------------------------------------------------------------------------------------------

To tackle this problem I suppose that the set S contains positive integers, sorted, with no duplicates.
Based on this assumption I can model the set S as an array of integer where each index represent the element
in S and the value represents a two-element list containing the predecessor and successor of that element.

For a set with 5 elements: S={0,1,2,3,4} I generate an array [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5]]
When an element is removed it is possible to access the element, get the index of the predecessor, go to the
predecessor and make its successor point to the element successor, then go to the elments successor 
make its predecessor point to the element predecessor.

To mark the element as removed it is possible to set to [] empty the associated list.
The complexity of the algorithm is O(1) since it only require access to the array element which
can be obtained in constant time.
'''

def remove(S, x):
    if S[x] == []: return False
    pre = S[x][0] #get the element predecessor
    suc = S[x][1] #get the elemnet successor
    S[pre][1] = suc #the predecessor successor now point to the element successor
    S[suc][0] = pre #the successor predecessor now point to the element predecessor
    S[x] = [] #set the element to empty
    return True

def find(S, x):
    if S[x] == [] or x<0 or x>len(S): return -1  
    return S[x][1] #return the successor

def main():

    N = 10
    S = [[n-1, n+1] for n in range(N)]
    S[0][0] = 0
    S[N-1][1] = N-1


    print "S = " + str(S)
    print "remove(8) = " + str(remove(S,8)) + "; S=" + str(S)
    print "remove(7) = " + str(remove(S,7)) + "; S=" + str(S)
    print "find(5) = " + str(find(S, 5))
    print "find(6) = " + str(find(S, 6))
    print "find(9) = " + str(find(S, 9))

if __name__ == "__main__":
    main()
