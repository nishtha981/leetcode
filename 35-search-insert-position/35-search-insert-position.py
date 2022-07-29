class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
 
        if(target<nums[0]):
            return 0
        elif(target>nums[-1]):
            return len(nums)
        else:
            for i in range(len(nums)-1):
                if nums[i]<target and nums[i+1]>target:
                    return i+1

            