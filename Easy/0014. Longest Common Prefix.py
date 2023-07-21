class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = ""
        if(len(strs[0]) < len(strs[len(strs) - 1])):
            length = len(strs[0])
        else:
            length = len(strs[len(strs) - 1])
        
        for i in range(length):
            if(strs[0][i] == strs[len(strs) - 1][i]):
                prefix += strs[0][i]
            else:
                break

        return prefix
        
