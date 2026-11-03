class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        seen= set()

        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        
        return result