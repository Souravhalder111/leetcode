class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        count = 1
        n1 = len(nums1)
        n2 = len(nums2)
        result = set()
        i = 0
        j = 0
        while(i < n1):
            if nums1[i] in hashmap:
                count += 1
                hashmap[nums1[i]] = count
            else:
                hashmap[nums1[i]] = count
            i += 1
        while(j < n2):
            if nums2[j] in hashmap:
                result.add(nums2[j])
            j += 1
        return list(result)