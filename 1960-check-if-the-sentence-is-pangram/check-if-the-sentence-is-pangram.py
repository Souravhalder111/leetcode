class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        map = [0] * 26
        for letter in sentence:
            map[ord(letter) - ord('a')] = 1

        for i in map:
            if(i == 0):
                return False
        else:
            return True