class Solution:

    def encode(self, strs: List[str]) -> str:
        # Check if list is empty
        if not strs:
            return ""
        
        res = ""

        # Get word lengths
        for i in strs:
            res += str(len(i)) + '.'
        res += '|'

        for i in strs:
            res += i 
        

        return res
      

    def decode(self, s: str) -> List[str]:
        ''' 
            - Parse the lengths first, then use those lengths to slice the string of words.
            1. Find the '|', separating the key to decoding from the actual words. Split by the '.' separator and convert to int.
            2. Use the lengths to slice the word string. Keep a pointer to your current position in the string..
               For each word, its [current_position + length]

        '''
        # Handle case of empty string ("")
        if not s:
            return []
        
        # Find delimiter |
        try:
            separator_index = s.index('|')
        except ValueError:
            # Handles cases where there is no '|', which means there is no length
            # information, likely a string like "" or "abc" that was not encoded
            if s == "":
                return [""]
            return [s]
        
        # Extract lengths and the string of words
        lengths_str = s[:separator_index]
        words_str = s[separator_index + 1:]

        print(lengths_str)
        print(words_str)

        # Handle edge case where original input was [""] -> "0,|"
        ...

        # Parse the lengths
        print(lengths_str.split('.'))
        sizes = [int(l) for l in lengths_str.split('.') if l]
        
        result = []
        current_index = 0

        for length in sizes:
            # Slice the string to get the word
            word = words_str[current_index : current_index + length]
            result.append(word)

            # Move the pointer forward
            current_index += length
        
        return result

