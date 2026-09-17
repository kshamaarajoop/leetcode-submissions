class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: list[int], idx: int):
            i = idx
            j = len(nums)-1
            while i<j:
                swap(nums,i,j)
                i+=1
                j-=1
        def swap(nums: list[int],i: int, j: int):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        idx = -1
        
        for i in range(len(nums)-2,-2,-1):
            print(i)
            if nums[i]<nums[i+1]:
                idx = i
                break
        if idx == -1:
            reverse(nums,0)
        else:
            #the next greater and swap
            for i in range(len(nums)-1,idx,-1):
                if(nums[i]>nums[idx]):
                    swap(nums,i,idx)
                    break
            reverse(nums,idx+1)
        
        

            
