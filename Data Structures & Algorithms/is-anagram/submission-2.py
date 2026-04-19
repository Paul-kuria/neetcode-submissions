class Solution:
    def helper(self, word: str):
        ''' Convert the characters in the word into a list of ascii numbers '''
        for i in word:
            print(i)
    
    def helper2(self, word: str):
        ''' Convert the string into a list of characters and sort in ascending order '''
        word_list = []
        for i in word:
            word_list.append(i)
        return sorted(word_list)

    def isAnagram(self, s: str, t: str) -> bool:
        word1 = self.helper2(s)
        word2 = self.helper2(t)

        # Compare the two lists to see if they are identical
        if word1 == word2:
            return True
        else:
            return False
       
