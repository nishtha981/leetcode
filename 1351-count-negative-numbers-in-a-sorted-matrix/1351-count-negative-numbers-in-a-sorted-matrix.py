class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        sum=0
        for i in grid:
            for j in i:
                if (j<0):
                    sum+=1
        return(sum)