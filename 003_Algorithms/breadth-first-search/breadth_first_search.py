from collections import deque

#Creating the graph manually
#The graph is the same used in Chapter 4.1 (page 533) of the book "Algorithm II"
vertex_list = [[2,1,5], [0,2], [0,1,3,4], [2,5,4], [2,3], [3,0]]
#List used to mark visited vertex
marked_list = [False, False, False, False, False, False]
#List used to sign from which node there was an incoming visit
#this list can be used to move backward from a given node.
edgeto_list = [-1, -1, -1, -1, -1, -1]

def breadth_first_search(s):
    queue = deque()
    queue.append(s)
    marked_list[s] = True
    print(s) #mark the starting node
    while(len(queue) != 0):
        v = queue.popleft() #important to pop-left (FIFO)
        adjacent_list = vertex_list[v] #get adjacent nodes
        for v_adj in adjacent_list:
            if marked_list[v_adj] == False:
                queue.append(v_adj)
                marked_list[v_adj] = True
                edgeto_list[v_adj] = v
                print(v_adj) #print marked node

print("Starting BFS algorith...")
print("Marked list:")
print marked_list
print("edgeto list:")
print edgeto_list
breadth_first_search(0)
print("Marked list:")
print marked_list
print("edgeto list:")
print edgeto_list
