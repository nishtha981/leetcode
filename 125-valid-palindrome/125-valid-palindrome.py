class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s1=""
        for i in range(len(s)):
            if s[i].isalnum()==True:
                s1+=s[i]
        s1=s1.lower()
        s=s1[::-1]
        if s1==s:
            return True
        else:
            return False
            
                