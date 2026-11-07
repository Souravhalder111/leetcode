class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        frequency_hashMap = {}

        for i in range(n):
            
            if s[i] in frequency_hashMap:
                frequency_hashMap[s[i]] += 1
            else:
                frequency_hashMap[s[i]] = 1
        
        for i in range(n):
            if(frequency_hashMap[s[i]] == 1):
                return i
        
        return -1