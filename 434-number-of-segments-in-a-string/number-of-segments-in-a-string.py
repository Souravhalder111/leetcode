class Solution:
    def countSegments(self, s: str) -> int:
        n = len(s)
        result = []
        segment = ""

        i = 0
        
        while(i < n):
            if(s[i] != " "):
                segment += s[i]
            else:
                if(segment != ""):
                    result.append(segment)
                    segment = ""
            
            i += 1
        
        if(segment != ""):
            result.append(segment)
        
        return len(result)