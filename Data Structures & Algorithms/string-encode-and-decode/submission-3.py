class Solution:

    def encode(self, strs: List[str]) -> str:
        # Initialize empty string to store encoded ans
        res = ""

        # Iterate through the strings in the list
        for item in strs:
            # string concatenation.
            # (length of word)+(delimiter)+(word)
            res  += str(len(item)) + "#" + item 
        return res 

    def decode(self, s: str) -> List[str]:
        # Initialize empty array to store words
        res = []

        # Initialize pointer
        i = 0

        # Iterate through the indexes of the string
        while i < len(s):
            # Initialize pointer j to help with string separation
            j=i
            # Inner while to check if delimiter has been found
            while s[j] != '#':
                j += 1
            
            # Found word length
            length = int(s[i:j])
            # Found word. j pointer +1 until j-pointer+1+word length.
            # Delimiter is at j, thus the j+1 is word start
            res.append(s[j+1:j+1+length])

            # Reset first pointer i to new word
            i = j+1+length
        return res