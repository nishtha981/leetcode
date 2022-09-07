class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        for i in nums:
            a=nums.count(i)
            if(a==1):
                return(i)
                