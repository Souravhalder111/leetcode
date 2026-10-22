class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote) > len(magazine)):
            return False
        
        hashset = [0] * 26

        for i in range(len(ransomNote)):
            if(hashset[ord(ransomNote[i]) - 97] != 0):
                hashset[ord(ransomNote[i]) - 97] += 1
            else:
                hashset[ord(ransomNote[i]) - 97] = 1
        
        for i in range(len(magazine)):
            hashset[ord(magazine[i]) - 97] -= 1
        
        for num in hashset:
            if(num > 0):
                return False
        
        return True