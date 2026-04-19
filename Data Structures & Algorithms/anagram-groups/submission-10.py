class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            k = tuple(sorted(s)) 
            
            if k not in hashmap:
                hashmap[k] = [s]
            else:
                hashmap[k].append(s)
        print(hashmap)
        return list(hashmap.values())