class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,res=0,0
        hMap = {}
        for r in range(len(s)):
            hMap[s[r]] = hMap.get(s[r],0) + 1
            #val = max(hMap, key=hMap.get)

            val = max(hMap.values())
            if ((r-l+1) - val) <= k:
                res = max(res, (r-l+1))
            else:
                hMap[s[l]] -= 1
                l += 1
                
        return res
        print(hMap,res)
