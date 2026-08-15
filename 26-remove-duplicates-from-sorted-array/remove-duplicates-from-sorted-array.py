class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        set1 = set(nums)
        for i in range(n):
            set1.add(nums[i])
        unique = sorted(set1)
        for j in range(len(unique)):
            nums[j] = unique[j]
        return len(unique)