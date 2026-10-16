class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        
        for char in s:
            if((not result) or char != result[-1]):
                result.append(char)
            else:
                result.pop()
        
        return "".join(result)