class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Create a list of buckets where index represents frequency [freq, number]
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        
        # Sort the array by frequency in ascending order
        arr.sort() 

        # Extract top K most frequent elements
        res = [] 
        while len(res) < k:
            # .pop() removes and returns the last element of the list.
            # We sorted in ascending order, so the last element is the most frequent.
            # We append the second element (the number) to the result.
            res.append(arr.pop()[1])
        return res

        
        
            
