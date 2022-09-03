class Solution:
    def isHappy(self, n: int) -> bool:
        
        already=[] 
        while(n!=0):
            sum=0
            for i in str(n):
                sum+=int(i)*int(i)
            n=sum
            if(n==1):
                return True
            elif(n in already):
                return False
            already.append(sum)