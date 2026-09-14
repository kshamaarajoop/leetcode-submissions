class Solution:
    def isPalindrome(self, s: str) -> bool:
        wrd = ""
        for s in s:
            if s.isalnum():
                wrd += s.lower()
        l = 0
        r = len(wrd) - 1
        while l<r:
            if wrd[l] != wrd[r]:
                return False
            r -= 1
            l += 1
        return True
