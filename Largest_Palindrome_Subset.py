# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:40:38 2016

@author: joby
"""


# Find the largest palindorme subset of a given string
def question2(string):
    """        
    palindrome list *pl* holds the palindrome length at each point.    
    (l for left end and r is right end of palindrome)    
    """
    sLen = len(string)
    pl = [] # extra storage of O(n)

    for i in range(2*sLen + 1):        
        l = i / 2 
        r = l + i % 2
        # in the above lines l ==r when i is even. If i is odd, r = l+1 .
        while r<sLen and l>0 and string[l - 1] == string[r]:
            l =l-1
            r =r+1
        pl.append(r - l) # length of the palindrom at i
    m = pl.index(max(pl)) # max index (gives center of biggest palindrome)
    l = m/2 -pl[m]/2
    # return the list of palindrome lengths and the longest palindrome
    return pl, string[l:(l+pl[m])]

if __name__ == "__main__":
   # Test Cases
   print question2('a')   # a
   print question2('madammadam') #'madamadam'
   print question2('abcdefghij') # Best case in time O(N)
   print question2('aaaaaaaaaaa')# Worst case in time O(N^2)
   
