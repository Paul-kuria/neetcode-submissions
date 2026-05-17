class Solution:
    def ascii_calculated(self, string: str):
        return tuple(sorted(string))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # If empty list
        if not strs:
            return [[""]]
        # If list has 1 item
        if len(strs) == 1:
            return [strs]
        
        hashmap = {}
        for item in strs:
            key = self.ascii_calculated(item)
            if key not in hashmap:
                hashmap[key] = [item]
            else:
                hashmap[key].append(item)
                
        values = list(hashmap.values())
        return values


        
