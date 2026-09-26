class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        amount = float("-inf")

        while(left < right):
            h = min(height[left], height[right])
            b = right - left
            area = h * b

            amount = max(amount, area)

            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        
        return amount