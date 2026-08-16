class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        result = set()
        i = 0
        while(i < n1):
            if nums1[i] in nums2:
                result.add(nums1[i])
            i += 1
        return sorted(result)