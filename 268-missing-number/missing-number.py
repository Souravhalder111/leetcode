class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0

        while(i <= n):
            if i not in nums:
                return i
            i += 1
        else:
            return 0
