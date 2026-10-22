class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote) > len(magazine)):
            return False
        
        array = [0] * 26

        n = len(ransomNote)
        m = len(magazine)

        for i in range(n):
            char_1 = ransomNote[i]

            if(array[ord(char_1) - 97] != 0):
                array[ord(char_1) - 97] += 1
            else:
                array[ord(char_1) - 97] = 1
        
        for i in range(m):
            char_2 = magazine[i]

            array[ord(char_2) - 97] -= 1
        
        for num in array:
            if(num > 0):
                return False
        
        return True