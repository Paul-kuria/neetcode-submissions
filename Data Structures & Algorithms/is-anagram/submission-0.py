class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cmp1 = {}
        cmp2 = {}

        for i in s:
            if i not in cmp1:
                cmp1[i] = 1
            else:
                cmp1[i] += 1
        
        for j in t:
            if j not in cmp2:
                cmp2[j] = 1
            else:
                cmp2[j] += 1        
        
        if cmp1 == cmp2:
            return True 
        else:
            return False