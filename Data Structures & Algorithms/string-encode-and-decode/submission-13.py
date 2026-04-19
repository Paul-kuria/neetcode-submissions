class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            length = str(len(word))
            ans += f"{length}:{word}"
        return ans 

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0 

        while index < len(s):
            # find end of the int
            j = index 
            while s[j] != ':':
                j += 1
            w_length = int(s[index:j])
            res.append(s[ j+1 : j+1+w_length])
            index = j + 1 + w_length
        return res
            

        # ans = []
        # p=0
        # for i in range(len(s)):
        #     count = int(s[p])
        #     i+=1
        #     if s[i] == ":":
        #         word = s[i+1:i+1+count]
        #         ans.append(word)
        #     p += i+1+count
