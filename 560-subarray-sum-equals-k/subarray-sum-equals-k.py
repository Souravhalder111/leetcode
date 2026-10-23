class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hashMap = {0 : 1}
        
        prefixSum = 0
        count = 0

        for i in range(n):
            prefixSum += nums[i]
            opposite = prefixSum - k

            if opposite in hashMap:
                count += hashMap[opposite]

            if prefixSum in hashMap:
                hashMap[prefixSum] += 1
            else:
                hashMap[prefixSum] = 1
        
        return count