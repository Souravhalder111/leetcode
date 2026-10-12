class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n-1
        i = n-1

        while(left <= right):
            if(nums[left]**2 <= nums[right]**2):
                result[i] = nums[right]**2
                i -= 1
                right -= 1
            else:
                result[i] = nums[left]**2
                i -= 1
                left += 1
            
        return result