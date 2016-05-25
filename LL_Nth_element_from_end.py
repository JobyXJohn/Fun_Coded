# -*- coding: utf-8 -*-
"""
Created on Mon May 23 10:10:57 2016

@author: joby
"""


# Node Definition     
class node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element    
            
# Main function answering Question 5
def question5(ll,nn):
    n = nn-1 # 1st element is zeroth index AS STATED in the QUESTION
    p1 = ll.head
    p2 = ll.head
    if n<0:
        print 'n has to be POSITIVE'
        return               
    if p1==None:
        print 'populate the list'
        return
    else:    
        for i in range(0,n): #advance p2 by n-1 positions
            if p2.next:
                p2=p2.next
               # print p2.value
            else:
                print 'WARNING: list size is smaller than n. Choose smaller n'
                return        
    while p2.next: #now advance both nodes till p2 reaches end
        p1=p1.next
        p2=p2.next
    return p1.value # p1 is now n positions from the end.    
            
if __name__ == '__main__':  
#create the node elemenmts
    e1 = node(10)
    e2 = node(20)
    e3 = node(30)
    e4 = node(40)
    e5 = node(0)
#setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    ll.append(e4)
    ll.append(e5)

# Test Cases  
    print '#### test 1 ##' 
    n=1
    n_element1 = question5(ll,1)
    print 'node at n=',1,' from end is ',n_element1,'\n'
    print '#### test 2 ##'  
    n_element2 = question5(ll,0)
    print 'node at n=',0,' from end is: ',n_element2, '\n'
    print '#### test 3 ##'  
    n_element3 = question5(ll,4)
    print 'node at n=',4,' from end is ',n_element3, '\n'
    print '#### test 4 ##'   
    n_element4 = question5(ll,5)
    print 'node at n=',5,' from end is ',n_element4, '\n'
    print '#### test 5 ##'  
    n_element5 = question5(ll,10)
    print 'node at n=',10,' from end is ',n_element5,'.',' See msg above.'
