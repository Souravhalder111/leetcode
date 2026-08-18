class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        for num in hashmap:
            if(hashmap[num] > int(n/2)):
                return num
        return -1