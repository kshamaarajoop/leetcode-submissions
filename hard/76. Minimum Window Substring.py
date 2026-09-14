class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap = {}
        need = {}
        if len(s)<len(t):
            return ""
        #initialising the hmap
        for i,nums in enumerate(t):
            hmap[nums] = hmap.get(nums,0)+1
        print(hmap)
        #sliing window
        l,r,match=0,0,0
        res = ""
        res_len = float("inf")
        while r < len(s):
            valid = True

            #adding r to the window
            need[s[r]] = need.get(s[r],0)+1
            #checking if the window is imilar to the required
            for char in hmap:
                if need.get(char,0) < hmap[char]:
                    valid = False
                    break
            while valid:
                if len(s[l:r+1])<res_len:
                    res = s[l:r+1]
                    res_len=len(res)
                #reduce the window size  move the window
                need[s[l]] -= 1
                l += 1

                # check validity AGAIN
                valid = True

                for char in hmap:
                    if need.get(char, 0) < hmap[char]:
                        valid = False
                        break
            r+=1

     
        return res
