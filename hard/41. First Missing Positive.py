class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hset = set(nums)
        for i in range(1,len(nums)+1):
            if i not in hset:
                return i
        return len(nums)+1
#this was def not hard, and it was not optimised at all so caution
