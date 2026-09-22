class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xorr = 0
        for letter1 in s:
            xorr ^= ord(letter1)
        
        for letter2 in t:
            xorr ^= ord(letter2)
        
        return chr(xorr)