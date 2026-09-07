class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            print(complement)
            if complement in hashMap:
                print("in for loop")
                return(i, hashMap.key(complement))
            hashMap[i] = i
        
