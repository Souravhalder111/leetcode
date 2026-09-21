class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        n = len(s)
        i = 0
        while(i < n):
            if(i < n-1 and dictionary[s[i]] < dictionary[s[i+1]]):
                result += dictionary[s[i+1]] - dictionary[s[i]]
                i += 2
            else:
                result += dictionary[s[i]]
                i += 1
        return result