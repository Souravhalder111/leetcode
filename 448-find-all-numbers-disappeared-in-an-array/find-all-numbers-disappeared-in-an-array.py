class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                continue
        
        result = []
        
        for i in range(1, n+1):
            if i not in seen:
                result.append(i)
        
        return result