class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead. 
        Dutch natural flag algo, 3 pointers
        """
        def swap(i: int, j: int):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
        
        l,r = 0, len(nums)-1
        curr = 0
        while curr<=r:
            if nums[curr]==0:
                swap(curr,l)
                l += 1
                curr += 1
            elif nums[curr]==2:
                #swap it with current high
                swap(r,curr)
                r -= 1
            else:
                #if curr is 1
                curr += 1
        return nums
        
