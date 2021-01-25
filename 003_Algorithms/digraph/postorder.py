

#Creating the graph manually
#The graph is the same used in Chapter 4.1 (page 533) of the book "Algorithm II"
vertex_list = [[1,5,2], [4], [], [4,5,2,6], [], [2], [0,4]]
#List used to mark visited vertex
marked_list = [False, False, False, False, False, False, False]
#List used to sign from which node there was an incoming visit
#this list can be used to move backward from a given node.
edgeto_list = [-1, -1, -1, -1, -1, -1, -1]
#the stack where we are gonna store the postorder values
postorder_list = list()

def depth_first_search(v):
    if marked_list[v] == False:
        marked_list[v] = True #mark the node
        #print(v) #print marked node
        adjacent_list = vertex_list[v] #get adjacent nodes
        for v_adj in adjacent_list:
            if marked_list[v_adj] == False:
                edgeto_list[v_adj] = v
                depth_first_search(v_adj) #iterative call
        postorder_list.append(v)
        print(v) #print the postorder node

print("Starting DFS algorith...")
print("Marked list:")
print marked_list
print("postorder list:")
print postorder_list
depth_first_search(0)
depth_first_search(3)
print("Marked list:")
print marked_list
print("postorder list:")
print postorder_list
