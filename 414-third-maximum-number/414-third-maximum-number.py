class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
       
        nums=set(nums)
        nums=sorted(nums, reverse=True)
        if(len(nums)>=3):
            return(nums[2])
        else:
            return(nums[0])