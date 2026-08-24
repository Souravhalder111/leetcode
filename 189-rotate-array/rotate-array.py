class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reverse(nums, low, high):
            while(low < high):
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)

        return nums
