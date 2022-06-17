class Solution:
    def isPalindrome(self, x: int) -> bool:
            
                check=x
                sum1=0
                while(x>0):
                        sum1=(sum1*10)+(x%10)
                        x=x//10
                if(sum1==check):
                    return True;
                else:
                    return False;
        