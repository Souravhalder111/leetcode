class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        i = 0
        while i < (2*n):
            if(i < n):
                ans.append(nums[i])
                i += 1
            else:
                ans.append(nums[i-n])
                i += 1
        return ans