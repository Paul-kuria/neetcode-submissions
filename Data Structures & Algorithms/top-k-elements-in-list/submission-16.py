class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = hashmap.get(num, 0) + 1
        
        # Initialize
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in hashmap.items():
            buckets[freq].append(num)
        
        # Reverse:
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
            
                if len(result) == k:
                
                    return result
                