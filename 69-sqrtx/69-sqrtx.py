class Solution:
    def mySqrt(self, x: int) -> int:
        
        i=0
        sqr=0
        while(sqr<=x):
            i+=1
            sqr=i*i  
        return(i-1)