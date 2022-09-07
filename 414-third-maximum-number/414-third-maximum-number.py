class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        a=sorted(nums, reverse=True)
        if(len(nums)>=3):
            return(a[2])
        else:
            return(a[0])