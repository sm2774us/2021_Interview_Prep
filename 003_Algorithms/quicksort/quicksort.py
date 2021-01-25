
from random import shuffle

class Quicksort():
    '''
    Quicksort is a recursive program that sorts a subarray a[lo..hi] by using a partition() method
    that puts a[j] into position and arranges the rest of the entries such that the recursive calls finish
    the sort.
    '''

    def sort(self, a):
        ''' it sorts the input array.

        '''
        #shuffle(a)
        self._sort(a, 0, len(a)-1)

    def _sort(self, a, lo, hi):
        if hi<= lo: return
        j = self._partition(a, lo, hi); 
        self._sort(a, lo, j-1) #Sort left part a[lo .. j-1].
        self._sort(a, j+1, hi) #Sort right part a[j+1 .. hi].

    #TODO check were the bug is...
    def _partition(self, a, lo, hi):
        i = lo
        j = hi
        v = a[lo] #partitioning item
        print i, j, v
        while(True):
            #Scan right
            while(a[i]<v):
                if i==hi: break
                i = i+1
            #scan left
            while(v<a[j]):
                if j==lo: break
                j = j-1
            print i, j, v
            print ""
            #Check for scan complete
            if i>=j: break
            #Exchange items
            #name[0], name[1] = name[1], name[0]
            print "Exchanging a[", j, "] and a[", i, "]"
            print a
            a[i], a[j] = a[j], a[i]
            print a   
            print "" 
            #temp_i = a[i]
            #temp_j = a[j]
            #a[i] = temp_j
            #a[j] = temp_i
        #Exchange items
        print "Exchanging a[", lo, "] and a[", j, "]"
        print a
        a[lo], a[j] = a[j], a[lo]
        print a   
        print ""  
        #temp_lo = a[lo]
        #temp_j = a[j]
        #a[lo] = temp_j
        #a[j] = temp_lo
        return j         


def main():
    a = [6,5,1,3,8,7,2,4]
    my_sorter = Quicksort()
    print a
    #my_sorter.TDsort(a, lo, hi)
    my_sorter.sort(a)
    print a

if __name__ == "__main__":
    main()
