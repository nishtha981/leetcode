class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum = 0
        i = 0
        if(n==1): return 1
        while(sum <= n):
            i += 1
            sum=((i*(i+1))/2)
        return(i-1)

        