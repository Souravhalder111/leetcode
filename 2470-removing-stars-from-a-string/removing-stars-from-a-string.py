class Solution:
    def removeStars(self, s: str) -> str:
        t = []

        for i in s:
            if(i == "*"):
                t.pop()
                continue
            t.append(i)

        result = ""
        
        for j in t:
            result += j

        return result