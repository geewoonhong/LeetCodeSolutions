/*
Given an integer array nums, move all the even integers
at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.



Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and
 [4,2,1,3] would also be accepted.

Note: The returned array must be malloced

 */

#include <stdlib.h>

int *sortArrayByParity(int *nums, int numsSize, int *returnSize)
{
	int	*res;
	int	rd;
	int wrtE;
	int wrtO;

	//update caller's variable to reflect size of returned array
	*returnSize = numsSize;
	rd = 0;
	wrtE = 0;
	wrtO = numsSize - 1;
	res = (int *)malloc(numsSize * sizeof(int));
	while (rd < numsSize)
	{
		if ((nums[rd] % 2) == 0) //if even
		{
			res[wrtE] = nums[rd];
			wrtE++;
			rd++;
		}
		else if((nums[rd] % 2 ) != 0) //is odd
		{
			res[wrtO] = nums[rd];
			wrtO--;
			rd++;
		}
	}
	return (res);
}
