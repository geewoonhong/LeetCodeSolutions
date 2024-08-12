/*
Given an integer array nums, move all 0's to the end of it
 while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
			  [0,1,12,3,0]
			  [3,1,12,0,0]
Output:       [1,3,12,0,0]
*/

void moveZeroes(int *nums, int numsSize)
{
    int rd;
	int wrt;

	rd = 0;
    wrt = 0;
	if (numsSize == 0)
		return ;
	while (rd < numsSize)
	{
		if (nums[rd] != 0)
		{
			nums[wrt] = nums[rd];
			wrt++;
			rd++;
		}
		else
			rd++;
	}
	while (wrt < numsSize)
	{
		nums[wrt] = 0;
		wrt++;
	}
	return ;
}
