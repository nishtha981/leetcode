class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s2 = ''.join(list(filter(lambda x: x.isalnum(), s))).lower()
        return s2 == s2[::-1]