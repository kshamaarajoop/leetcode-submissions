class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        #sliding window
        i = 0
        k = 1
        m = 1
        while i < len(nums) and k < len(nums):
            if (nums[k] - nums[k-1]) <= 1:
                k += 1
            else:
                i = k
                k += 1
            m = max(m,k-i)
        return m
