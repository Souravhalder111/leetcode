class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        left = 0
        right = n-1

        while(left < right):
            
            s[left], s[right] = s[right], s[left]     # Swap the elements

            left += 1                                 # Increment the first pointer
            right -= 1                                # Decrement the last pointer
        
        return s