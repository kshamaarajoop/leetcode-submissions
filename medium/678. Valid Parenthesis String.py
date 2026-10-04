class Solution:
    def checkValidString(self, s: str) -> bool:
        maxm,minm=0,0
        for c in s:
            if c == "(":
                maxm += 1
                minm += 1
            elif c == ")":
                maxm -= 1
                minm -= 1
            else:
                # * can be ) , (  or empty
                maxm += 1
                minm -= 1
            if maxm<0:
                return False
            minm = max(minm,0)
        return minm == 0
