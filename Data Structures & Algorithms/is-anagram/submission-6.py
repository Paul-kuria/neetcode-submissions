class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Input: strings s & t
        Output: boolean
        TESTING: anagrams (string that contains same characters as another string)
        '''
        if len(s) != len(t):
            return False 
            
        hashtable1 = {}
        hashtable2 = {}
        s = sorted(s)
        t = sorted(t)
        # Populate dict
        for char in s:
            if char not in hashtable1:
                hashtable1[char] = 1
            else:
                hashtable1[char] += 1
        
        for char in t:
            if char not in hashtable2:
                hashtable2[char] = 1
            else:
                hashtable2[char] += 1
                
        if hashtable1 == hashtable2:
            return True
        else:
            return False

            
            


