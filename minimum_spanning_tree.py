"""
Created on Mon May 16 18:05:53 2016

@author: joby
"""
#Input is a graph in the form of an adjacency list 
    #This is a dictionary with the node name as keys and the adjacent elements
    # and weights as a list forming the value of the key.
# Output is an adjacency list of the minimum-spanning tree.
    # This is also a dictionary with the node name as key and only the adjacent 
    # node with the smallest weight as the value

def question3(G):
    nodeheap = []
    mst = {}
    for node in G: # loops through dictionary keys (node names)               
        nodeheap.append((node,float('inf'))) # assign infinity to all values
    
    try:# Check that the graph has nodes    
        nodeheap[0]=(nodeheap[0][0],0) # Assign 0 to first value 
        minnode = nodeheap[0]
    except (KeyError,IndexError):
        print 'node heap must have atleast one node'
    # assign the first node with zero value to minimum
    else:
        while nodeheap:       # continue till all nodes are assigned to MST
            pnode = minnode[0] # save the previous node             
            minnode =nodeheap.pop(nodeheap.index(
                        min(nodeheap,key=lambda tup: tup[1]))) # pop the smallest element
            mst[pnode]=[minnode] #assign the minnode to MST
            for edge in G[minnode[0]]: # Scan through edges
                for idx in range(len(nodeheap)): 
                    if nodeheap[idx][0]==edge[0] and nodeheap[idx][1] >edge[1]:# see if edge already in MST
                        nodeheap[idx]=(nodeheap[idx][0],edge[1])
                        break # discontinue for-loop, value assigned in heap      
    return mst    
#######################################    
if __name__ =="__main__":
    print '######### test1 #########'
    # a graph with five nodes
    G1 = {'A':[('B',5),('D',5)],'B':[('A',5),('C',3),('D',2)],
          'C':[('B',3),('E',1)],'D':[('B',2),('A',5),('E',5)],'E':[('C',1),('E',5)]}
    MST = question3(G1)  
    print 'MST is ', MST,'\n'
    ######################################
    print '######### test2 #########'
    # MST is same as graph    
    G2 = {'A':[('B',1)],'B':[('D',2),('C',2)],'C':[('A',2),('D',2)],'D':[('B',2),('C',2)]}
    MST2 = question3(G2)
    print 'MST is ', MST2,'\n'
    #####################################
    print '######### test3 #########'
    # Empty Graph
    G3={}
    MST3 = question3(G3);
    print 'MST is', MST3
