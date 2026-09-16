class Solution:
    def trap(self, height: list[int]) -> int:
        l,r,tot = 0, len(height)-1, 0
        lmax,rmax = 0, 0
        while l<=r:
            if height[l]<height[r]:
                if lmax > height[l]:
                    tot += lmax - height[l]
                else:
                    lmax = height[l]
                l+=1
            else:
                if rmax > height[r]:
                    tot += rmax - height[r]
                else:
                    rmax = height[r]
                r-=1
        return tot
        
