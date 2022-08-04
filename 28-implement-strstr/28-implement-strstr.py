class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       
        x= lambda a, b: a.index(b) if(b in a) else -1
        return(x(haystack,needle))