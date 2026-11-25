class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n * 2

        for i in range(n):
            ans[i] = nums[i]
            ans[(2*n) - i - 1] = nums[i]

        return ans 