

#Creating the graph manually
#The graph is the same used in Chapter 4.1 (page 533) of the book "Algorithm II"
vertex_list = [[6,2,1,5], [0], [0], [5,4], [5,6,3], [3,4,0], [0,4], [8], [7], [10,12,11], [9], [9,12], [11,9]]
#List used to mark visited vertex
marked_list = [False, False, False, False, False, False, False, False, False, False, False, False, False]
#List used to sign from which node there was an incoming visit
#this list can be used to move backward from a given node.
edgeto_list = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
#Variables for the connected components
cc_counter = 0
cc_list = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

def depth_first_search(v):
    if marked_list[v] == False:
        marked_list[v] = True #mark the node
        print(v) #print marked node
        adjacent_list = vertex_list[v] #get adjacent nodes
        for v_adj in adjacent_list:
            if marked_list[v_adj] == False:
                edgeto_list[v_adj] = v
                depth_first_search(v_adj) #iterative call
                #Additional code for connected components
                cc_list[v_adj] = cc_counter


for v in range(len(marked_list)):
    if marked_list[v] == False:
        cc_list[v] = cc_counter #assign the ID to the starting node
        depth_first_search(v) #depth search from the starting node
        cc_counter += 1 #increment the ID counter

print("Starting DFS algorith...")
print("Marked list:")
print marked_list
print("edgeto list:")
print edgeto_list
print("cc list:")
print cc_list

depth_first_search(0)

print("Marked list:")
print marked_list
print("edgeto list:")
print edgeto_list
print("cc list:")
print cc_list
