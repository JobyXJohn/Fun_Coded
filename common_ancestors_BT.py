
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 8:08:48 2016

@author: joby
"""


"""
Binary tree shown below is used in test cases
            3
           / \
             
         0     2
        / \     \
               
       4   1     6
          / \
          
         5   7

"""
import numpy as np
'''
The function question4 has space complexity O(n)
'''
def question4(T,r,n1,n2):
    countlist=np.zeros(T.shape[0])# N elements         
    while 2 not in countlist:       
        if n1 == n2:
            break
        if n1==r or n2==r:
            n2=r # the root is now stored in n2.
            break 
        n1 =[i for i, e in enumerate(T[:,n1]) if e != 0][0]
        countlist[n1]+=1        
        if n1!=n2: 
            n2 = [i for i, e in enumerate(T[:,n2]) if e != 0][0]                
            countlist[n2]+=1
    return n2

'''The following function question4_better() has a space complexity of O(log N).
'''
def question4_better(T,r,n1,n2):
    n1parents = [n1] # These two list are at most log N elements.
    n2parents = [n2] # Compare to countlist in question4()
    while n1 not in n2parents and n2 not in n1parents and not (n1==r and n2==r):       
        if n1 !=r:        
            n1 =[i for i, e in enumerate(T[:,n1]) if e != 0][0]
            n1parents.append(n1)
        if n2 !=r:
            n2 = [i for i, e in enumerate(T[:,n2]) if e != 0][0]                
            n2parents.append(n2)
    return n2 if n2 in n1parents else n1

if __name__ == "__main__":
    T= [[0,1,0,0,1,0,0,0],
        [0,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,0],
        [1,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
    T=np.array(T)
    r=3
    print '#### question4() ####'
    print '## test 1 ##'
    # two different nodes (non-root LCA)
    LCA = question4(T,r,4,7)
    print 'The LCA is ', LCA, '\n'
    #############################
    print '## test 2 ##'
    # both nodes are equal. LCA is the same node. 
    LCA = question4(T,r,4,4)
    print 'The LCA is ', LCA, '\n'
    ############################
    print '## test 3 ##'
    ## Far apart
    LCA = question4(T,r,5,6)
    print 'The LCA is ', LCA,'\n'
    ##############################
    print '## test 4 ##'
    ## order switched
    LCA = question4(T,r,2,5)    
    print 'The LCA is ', LCA,'\n'
    ############################
    print '## test 5 ##'
    LCA = question4(T,r,5,7)    
    print 'The LCA is ', LCA,'\n'
    ## ************************* ##
    ## ************************* ##
    print '*************************'
    print '#### question4_better()##'
    print '## test 1 ##'
    # two different nodes (non-root LCA)
    LCA = question4(T,r,4,7)
    print 'The LCA is ', LCA, '\n'
    #############################
    print '## test 2 ##'
    # both nodes are equal. LCA is the same node. 
    LCA = question4(T,r,4,4)
    print 'The LCA is ', LCA, '\n'
    ############################
    print '## test 3 ##'
    ## Far apart
    LCA = question4(T,r,5,6)
    print 'The LCA is ', LCA,'\n'
    ##############################
    print '## test 4 ##'
    ## order switched
    LCA = question4(T,r,6,5)    
    print 'The LCA is ', LCA,'\n'
    ##############################
    print '## test 5 ##'
    LCA = question4(T,r,5,7)    
    print 'The LCA is ', LCA
