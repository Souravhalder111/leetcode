class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False

        new_string = s + s
        
        if goal in new_string:
            return True

        return False