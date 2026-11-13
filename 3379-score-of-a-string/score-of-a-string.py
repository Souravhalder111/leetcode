class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        result = 0

        for i in range(n-1):
            value = abs(ord(s[i]) - ord(s[i+1]))
            result += value
            
        return result