class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        xorr = 0

        for i in range(n):
            xorr ^= nums[i]
            xorr ^= (i+1)
        
        return xorr