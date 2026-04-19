class Solution:
    def ascii_helper(self, word: str)->int:
        ''' Convert each word to a total of its individual ascii character sums for anagram match checking'''
        total:int=0
        for i in word:
            total += ord(i)
        return total

    def sorted_helper(self, word: str):
        return sorted(word)
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize hashmap to store the ascii value, and names that match that value
        matches: dict = {}

        # # Iterate through list of strings
        # for name in strs:
        #     # Extract ascii sum of each word
        #     name_ascii = self.ascii_helper(name)

        #     # Begin appending to hashmap, key is the ascii-value, value is the list of words that are anagrams
        #     if name_ascii not in matches:
        #         matches[name_ascii] = [name]
        #     else:
        #         matches[name_ascii].append(name)

        for name in strs:
            # Get sorted name as a list
            sorted_name = tuple(self.sorted_helper(name))

            if sorted_name not in matches:
                matches[sorted_name] = [name]
            else:
                matches[sorted_name].append(name)


            

        # Extract just the values
        ans = []
        for k, v in matches.items():
            ans.append(v)
        return ans