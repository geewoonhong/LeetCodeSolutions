/*

Given an int array, return the third distinct max num in the array
if the third max num does not exist return the maximum num
Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist,
so the maximum (2) is returned instead.

Constraints:

1 <= nums.length <= 104
-2^31 <= nums[i] <= 2^31 - 1
*/
#include <stdio.h>

int thirdMax(int *nums, int numsSize)
{
	int i=0, j=0, box=0, count=1;

	while (i < numsSize)
	{
		while (j < numsSize -1)
		{
			if (nums[j] < nums[j+1])
			{
				box = nums[j+1];
				nums[j+1] = nums[j];
				nums[j] = box;
			}
			j++;
		}
		j = 0;
		i++;
	}
	i = 1;
	while (i<numsSize)
	{
		if(nums[i] < nums[i-1])
			count++;
		if(count == 3)
			return(nums[i]);
		i++;
	}
	return (nums[0]);
}

int main() {
    int nums[] = {3, 2, 1};
    int size = sizeof(nums) / sizeof(nums[0]);
    int result = thirdMax(nums, size);

    printf("The third distinct maximum is: %d\n", result);  // Output should be 4

    return 0;
}

// int	thirdMax(int *nums, int numsSize)
// {
// 	int unqMax1 = INT_MIN;
// 	for (int i = 0; i < numsSize; i++)
// 	{
// 		if (nums[i] >= unqMax1)
// 			unqMax1 = nums[i];
// 	}

// 	int unqMax2 = INT_MIN;
// 	for (int i = 0; i < numsSize; i++)
// 	{
// 		if (nums[i] >= unqMax2 && nums[i] != unqMax1)
// 			unqMax2 = nums[i];
// 	}

// 	int unqMax3 = INT_MIN;
// 	for (int i = 0; i < numsSize; i++)
// 	{
// 		if (nums[i] >= unqMax3 && nums[i] != unqMax1 && nums[i] != unqMax2)
// 			unqMax3 = nums[i];
// 	}

// 	if

// 	return (unqMax3);
// }
