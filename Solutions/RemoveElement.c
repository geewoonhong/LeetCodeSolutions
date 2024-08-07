
/*
example
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
*/

int removeElement(int* nums, int numsSize, int val) {
    int i = 0;
    int k = 0;
    while (i < numsSize)
    {
        if (nums[i] != val)
        {
            nums[k] = nums[i];
            k++;
        }
        i++;
    }
    return (k);
}
