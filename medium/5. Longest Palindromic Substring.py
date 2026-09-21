class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            #for ordd
            if len(ans) < len(self.checkPalindrom(s,i,i)):
                ans = self.checkPalindrom(s,i,i)

            if len(ans) < len(self.checkPalindrom(s,i,i+1)):
                ans = self.checkPalindrom(s,i,i+1)
        return ans

    def checkPalindrom(self,s: str,i: int, j: int):
        while i>=0 and j<len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        i += 1
        j -= 1
        return s[i:j+1]

        
        
