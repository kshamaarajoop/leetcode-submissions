class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for words in strs:
            i = 0
            while i<len(prefix) and i<len(words):
                if words[i] == prefix[i]:
                    i+=1
                    continue
                else:
                    prefix = prefix[:i]
                    i+=1
                    break
            prefix = prefix[:i]
        return prefix

        
