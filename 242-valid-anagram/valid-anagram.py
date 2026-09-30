class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        hashMap = {}
        
        for i in s:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
            
        for j in t:
            if j in hashMap:
                hashMap[j] -= 1
            else:
                hashMap[j] = 1
            
        for k in hashMap:
            if(hashMap[k] != 0):
                return False
        
        return True