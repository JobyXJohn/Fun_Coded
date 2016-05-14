"""
Created on Wed May 11 17:00:35 2016

@author: joby
"""
# Find if one string is a palindrome subset of another
## ASSUME NO SPACES IN BOTH STRINGS
#import numpy as np
def question1(s=None, t=None):    
    anagram_count =0 # variable counts the number of anagrams
    try:
        s=s.lower()
        t=t.lower()
        M = len(t)
        N = len(s)        
        if N < M: # assume M has to be less than N
            print 'provide a shorter "second" string'
            return False
        elif M <1 or N <1:
            print 'string needs to have atleast one character'
            return False           
    except:
        print 'Provide two strings as arguments'#,ex
    else:
        # Assume the alphabet set is 256 long. Reasonable assumption
        # The two lists keep a count of each alphabet (indexed at the ascii value)
        charT = [0]*256 
        charS = [0]*256
        
        # populate the count lists; First M =len(t) characters.
        for i in range(len(t)):
            charT[ord(t[i])]+=1
            charS[ord(s[i])]+=1       
        
        for i in range(M,len(s)): # loop over the remaining chars in s
            if charT>0 and charT==charS:
                print "Anagram of",'"',t,'"', "at index ", i-M, " of string big string",'"',s,'"'
                #print np.where(np.array(charT)>0),np.where(np.array(charS)>0)
                anagram_count+=1
            charS[ord(s[i])]+=1
            charS[ord(s[i-M])]-=1
        if charT>0 and charT==charS:
            print "Anagram",'"',t,'"', "at index ", N-M," of string big string",'"',s,'"'
            anagram_count+=1
    
    if anagram_count >0:
        print "Number of Anagrams of ", anagram_count        
        return True        
    else:
        return False        
            
if __name__ == "__main__":
# Test CAses    
    print question1('****ClintEastwood***EastwoodClint','OldWestAction'),'\n','####################\n'
    # True          
    print question1('udacity','sity'), '\n','####################\n'
    # False        
    print question1('udacityac','acity'),'\n','####################\n'
    # True
    print question1('abc','abcd'), '\n','####################\n'
    # Error
    print question1('abc',''),'\n','####################\n'
    # Error
    print question1('abc'),'\n','####################\n'
    # anagram at all locations
    print question1('aaaaa','aa'),'\n'
    
    
