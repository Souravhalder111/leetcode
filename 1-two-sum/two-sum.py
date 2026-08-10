class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        map = {}
        for i in range(n):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            else:
                map[nums[i]] = i