#HashSet
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            hashMap.add(nums[i])
        return False
#HashMap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            hashMap[nums[i]] = i
        return False
#two pointers - SC 0(1) TC O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 1
        while i<len(nums):
            if nums[i-1]==nums[i]:
                return True
            i += 1
        return False
