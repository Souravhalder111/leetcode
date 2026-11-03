class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        
        for num in nums:
            x = abs(num)
            if(nums[x-1] < 0):
                result.append(x)
            nums[x-1] *= -1
        
        return result