class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        copied_string = s.copy()
        for i in range(n-1, -1, -1):
            s[n-i-1] = copied_string[i]
        return s