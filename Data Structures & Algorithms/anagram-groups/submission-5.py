class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize hashmap
        ans = {}

        # Loop through the words in the list
        for word in strs:
            # Initialize list of lowercase characters placeholders per word
            count_char = [0] * 26
            
            # Loop through the characters in each word
            for ch in word:
                # Add 1 in the index of each character for this word
                count_char[ord(ch)-ord('a')] += 1
            
            # Convert list to tuple to make it hashable
            count_char = tuple(count_char)

            # Add k,v to hashmap
            if count_char not in ans:
                # set the count_char as key and initialize an empty list
                ans[count_char] = []
            # Add words to the count_char keys that are similar
            ans[count_char].append(word)
        return list(ans.values())