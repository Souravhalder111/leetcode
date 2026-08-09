class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            num1 = nums[i]
            num2 = target - num1
            if num2 in nums:
                j = nums.index(num2)
                if i != j:
                    return [i, j]