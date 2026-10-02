class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()

        result = (nums[n-1] - 1) * (nums[n-2] - 1)

        return result