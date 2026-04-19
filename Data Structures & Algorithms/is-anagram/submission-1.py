class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 strings return true if the 2 are anagrams of each other.
        comp1 = {}
        comp2 = {}

        for i in s:
            if i not in comp1:
                comp1[i] = 1
            comp1[i] += 1
        
        for j in t:
            if j not in comp2:
                comp2[j] = 1
            comp2[j] += 1

        print(comp1)
        print(comp2)

        if comp1 == comp2:
            return True
        else:
            return False