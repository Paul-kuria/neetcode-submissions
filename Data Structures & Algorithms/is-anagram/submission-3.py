class Solution:
    def create_hash(self, string: str, hash: dict):
        for i in string:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        return hash

    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        h1 = self.create_hash(s, hash1)
        h2 = self.create_hash(t, hash2)

        # Check 1:
        if len(h1) != len(h2):
            return False
        
        # Check 2:
        if h1 != h2:
            return False
        
        return True

