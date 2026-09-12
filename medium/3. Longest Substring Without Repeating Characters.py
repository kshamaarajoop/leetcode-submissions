class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hSet = set()
        l,r = 0,0
        mlen = 0
        while r < (len(s)):
            if s[r] not in hSet:
                hSet.add(s[r])
                mlen = max(len(hSet),mlen)
                r += 1
            else: 
                hSet.discard(s[l])
                l += 1
        return mlen
