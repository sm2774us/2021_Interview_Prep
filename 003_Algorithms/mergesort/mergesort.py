

class Mergesort():

    def TDsort(self, a, lo, hi):
        ''' it sort the input array in top-down order.

        Based on the lo and hi variables it sorts the values inside a.
        The array a is divided in two halves and sorted recursively.
        '''
        if hi <= lo: return #termination condition for the recursion
        mid = int(lo + (hi - lo)/2) #estimates the mid point
        self.TDsort(a, lo, mid) #sort the left half
        self.TDsort(a, mid+1, hi) #sort the right half
        self._merge(a, lo, mid, hi) #merge the results

    def BUsort(self, a):
        ''' it sort the input array in bottom-up order.

        Based on the lo and hi variables it sorts the values inside a[].
        The array a is divided in two halves and sorted recursively.
        '''
        N = len(a)
        #sz = sub-array size
        #lo = sub-array index
        for sz in range(1, N):

            for lo in range(0, N-sz):
                mid = lo+sz-1 #5, 9, 13, 
                hi = min(lo+sz+sz-1, N-1) #7, 11, 
                self._merge(a, lo, mid, hi)
                lo += sz+sz #4, 8, 12, 16, 20
                print lo, mid, hi
                print(a)
            sz = sz+sz #2, 4, 6, 8, 10, 12, 14, 16, 18,

    def _merge(self, a, lo, mid, hi):
        ''' it merges the input array.

        Based on the lo, hi and mid point it merges the values of the array.
        The array a is divided in two halves and sorted recursively.
        '''
        i = lo
        j = mid+1
        #clone the list
        aux = a[:]
        #for k in range(lo, hi+1):
        #    aux[k] = a[k]
        #here elements in a[] are replaced with the largest
        #element obtained from the comparison of a[] and aux[]
        for k in range(lo, hi+1):
             if i>mid: 
                 a[k] = aux[j]
                 j += 1 #left half exhausted
             elif j>hi: 
                 a[k] = aux[i]
                 i += 1 #right half exhausted
             elif aux[j] < aux[i]: 
                 a[k] = aux[j]
                 j += 1 #right value less than left value
             elif aux[j] >= aux[i]: 
                 a[k] = aux[i]
                 i += 1; #right value greater or equal to left value


def main():
    a = [6,5,1,3,8,7,2,4]
    my_sorter = Mergesort()
    lo = 0
    hi = len(a)-1 # hi ==> 12-1 = 11
    print a
    #my_sorter.TDsort(a, lo, hi)
    my_sorter.BUsort(a)
    print a

if __name__ == "__main__":
    main()
