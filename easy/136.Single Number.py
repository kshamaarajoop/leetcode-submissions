class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 1

        while i < len(nums):
            if nums[i-1] == nums[i]:
                
                print(nums[i-1])
                print(nums[i])
                i += 2
                print(i)
            else:
                return nums[i-1]
        return nums[len(nums)-1]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res


