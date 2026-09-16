class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(map(str, s.split()))
        n = len(s)
        return len(s[n-1])