class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor1 = 0
        for i in range(n):
            xor1 = xor1 ^ nums[i]
        return xor1