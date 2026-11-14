class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        mini = min(nums)

        result = []
        seen = set(nums)

        for i in range(mini, maxi):
            if i not in seen:
                result.append(i)
            else:
                continue
        
        return result