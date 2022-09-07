class Solution:
    def addDigits(self, num: int) -> int:
        
        while(num>9):
            total=0
            while(num>0):
                n=num%10
                num=num//10
                total+=n
            num=total
        return num