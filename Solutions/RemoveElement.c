
/*
example
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
*/
#include <stdio.h>

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

void	printArray(int *array, int size)
{
	int i = 0;
	while (i < size)
	{
		printf("%d ", array[i]);
		i++;
	}
	printf("\n");
}

int	main()
{
	int tst1[] = {3,2,2,3};
	int tst2[] = {1,2,2,3,5,3,2};
	int tst3[] = {1,2,2,2,2,1,2,1,1,2,1,1,4,5,6,8,2,10,2};

	int size1 = sizeof(tst1) / sizeof(tst1[0]);
	int size2 = sizeof(tst2) / sizeof(tst2[0]);
	int size3 = sizeof(tst3) / sizeof(tst3[0]);

	int newsize1 = removeElement(tst1, size1, 3);
	int newsize2 = removeElement(tst2, size2, 3);
	int newsize3 = removeElement(tst3, size3, 2);

	printf("After modification for tst1: ");
	printArray(tst1, newsize1);
	printf("After modification for tst2: ");
	printArray(tst2, newsize2);
	printf("After modification for tst3: ");
	printArray(tst3, newsize3);
	return (0);
}
