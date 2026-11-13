class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = len(nums)
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        
        return result