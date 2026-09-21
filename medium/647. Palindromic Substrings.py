class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            #odd palindrome
            ans += self.checkPalindrome(s,i,i)
            #even palindrome case
            ans += self.checkPalindrome(s,i,i+1)
        return ans
    def checkPalindrome(self,s: str, i: int, j: int):
        count = 0
        while i >= 0 and j <len(s) and s[i] == s[j]:
            count +=1 
            i -= 1
            j += 1
        return count
        
