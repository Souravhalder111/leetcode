class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppercase = 0

        for char in word:
            if(char.isupper()):
                uppercase += 1
        
        return uppercase == len(word) or uppercase == 0 or (uppercase == 1 and word[0].isupper())