class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        nums.sort()

        result = []

        for i in range(n):
            if(nums[i] == target):
                result.append(i)
        
        return result