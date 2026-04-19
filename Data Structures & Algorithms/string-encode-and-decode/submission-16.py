class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word 
        return res 

    def decode(self, s: str) -> List[str]:
        # Initialize empty list and pointer 2
        ans = []
        i = 0
        print(s)
        # Iterate over word
        while i < len(s):
            # Step 1: Find where '# is. Assign j to the new letter i value
            j = i
            
            while (s[j] != "#"):
                j += 1
            
            # Step 2: Get word length
            length = int(s[ i:j ])

            # Step 3: Extract the word. Starts right after '#' and goes for 'length' characters
            word = s[ j+1: j+1+length ]
            print(length, word)
            ans.append(word)
            i = j + 1 + length 
        return ans

 