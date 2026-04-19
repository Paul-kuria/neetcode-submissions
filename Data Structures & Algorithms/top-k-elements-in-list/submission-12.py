class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create hash table
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Create a bucket sort placeholder list with the frequencies 
        frequencies = [ [] for i in range(len(nums)+1) ]

        # Place the numbers in the frequencies list
        for num, freq in count.items():
            frequencies[freq].append(num)
        
        # Extract first k nums:
        ans = []
        for i in range(len(frequencies)-1, 0, -1):
            bucket = frequencies[i]
            if bucket:
                for n in bucket:
                    ans.append(n)

                if len(ans) == k:
                    return ans
                
