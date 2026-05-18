from typing import List, Dict
class Solution:

    def encode(self, s: list)->str:
        # Case list is empty
        if not s:
            return ""
        
        # Initialize list
        strs = ""
        
        # Use '#' as separator of word count and word
        for word in s:
            strs += str(len(word))  + "#" + word 
        
        return strs 
    
    def decode(self, s: str):
        # Case, string is empty
        if not s:
            return []
            
        print(f"Encoded: {s}")
        # Init
        ans = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            i = j + 1
            word = s[ i : i+length ]
            ans.append(word)
            
            # Move i forward, already saved word.
            i += length
            
        return ans
