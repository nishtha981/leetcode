int removeDuplicates(int* nums, int numsSize){
    int old=0;
    for (int i = 1; i < numsSize; i++)
    {
        if (nums[i - 1] < nums[i])
        {
            nums[++old] = nums[i];
        }
    }
    return(old+1);
}