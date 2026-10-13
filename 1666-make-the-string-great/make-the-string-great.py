class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        new_string = []

        for i in range(n):
            if(new_string and abs(ord(new_string[-1]) - ord(s[i])) == 32):
                new_string.pop()
                continue
            else:
                new_string.append(s[i])
        
        return "".join(new_string)