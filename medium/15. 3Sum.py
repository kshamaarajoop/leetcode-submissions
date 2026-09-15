#optimised a little but not much imporvement
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #fixing one number and attempting to fin th rest
        res = set()
        nums.sort()
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
          #breaking after postive number encountered
            if nums[i]>0:
                break
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    
                    if nums[l] == nums[l + 1]:
                        l += 1

                    # Skip duplicate right values
                    if nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
                
        return [list(x) for x in res]
                                       

#unoptimised solution
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #fixing one number and attempting to fin th rest
        res = set()
        nums.sort()
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l < r:
                
                if nums[i]+nums[l]+nums[r] == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                else:
                    l += 1
                
        return [list(x) for x in res]
                                       
