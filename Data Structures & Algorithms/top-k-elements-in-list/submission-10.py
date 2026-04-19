class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count frequencies
        hash = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        
        # create list of [freq, number] pairs
        freq_pairs = [[freq, num] for num, freq in hash.items()]
        
        # Sort by frequency in desc order
        freq_pairs.sort(reverse=True)
        print(freq_pairs)
        # Get top k elements (just. the numbers)
        res = []

        for i in range(k):
            print(i, k, freq_pairs[i])
            res.append(freq_pairs[i][1])
        return res
        
    
