/*
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should
be kept the same. Then return the number of unique elements in nums.
*/
#include <stdio.h>

// int removeDuplicates(int *nums, int numsSize)
// {
//     int i = 0;
//     int k = 0;
//     while (i < numsSize)
//     {
//         if (((i+1) < numsSize) && (nums[i] != nums[i+1]))
//         {
//             nums[k] = nums[i];
//             k++;
//         }
// 		else if((i+1) == numsSize)
//         {
// 			nums[k] = nums[i];
// 			k++;
//         }
// 		i++;
//     }
//     return (k);
// }

int	removeDuplicates(int *nums, int numsSize)
{
	int	writeptr;
	int	readptr;

	writeptr = 1;
	readptr = 1;
	while (readptr < numsSize)
	{
		if (nums[readptr] != nums[readptr -1]) //if it is a unique number
		{
			nums[writeptr] = nums[readptr];
			writeptr++;
			readptr++;
		}
		else
			readptr++;
	}
	return (writeptr);
}

/* Another faster method */
// int removeDuplicates(int* nums, int numsSize) {
//     int i =0;
//     int count=-1000;
//     int j=0;
//     int counter=0;
//     for(i=0; i < numsSize; i++)
// 	{
//        if(nums[i] > count)
// 	   {
//         counter++;
//         count = nums[i];
//         nums[j]=count;
//         j++;
//        }
//     }
//     return counter;

// }

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

int main()
{
	int tst1[] = {1,1,2};
	int tst2[] = {0,0,1,1,1,2,2,3,3,4};

	int size1 = sizeof(tst1) / sizeof(tst1[0]);
	int size2 = sizeof(tst2) / sizeof(tst2[0]);

	int newsize1 = removeDuplicates(tst1, size1);
	int newsize2 = removeDuplicates(tst2, size2);

	printf("After modification for tst1: ");
	printArray(tst1, newsize1);
	printf("After modification for tst2: ");
	printArray(tst2, newsize2);
	return (0);
}
