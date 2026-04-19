class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for item in strs:
            count = [0]*26
            for c in item:
                count[ord(c)-ord('a')] += 1
            if tuple(count) not in ans:
                ans[tuple(count)] = [item]
            else:
                ans[tuple(count)].append(item)

        return (ans.values())