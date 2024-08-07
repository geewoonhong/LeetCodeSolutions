int removeElement(int* nums, int numsSize, int val) {
    int i = 1;
    int k = 0;
    while (i < numsSize)
    {
        if (nums[i] != nums[i-1])
        {
            nums[k] = nums[i];
            k++;
        }
        i++;
    }
    return (k);
}
