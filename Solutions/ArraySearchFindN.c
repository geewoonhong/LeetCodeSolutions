/*
Given an arr of int, check if two indicies i and j exist in the arr:
i != j
0 <= i	j < arr_len
arr[i] == 2*arr[j]
*/

#include <stdio.h>
#include <stdbool.h>


bool checkIfExist(int *arr, int arrSize)
{
	int i, j;

	i, j = 0;
	if (arr == NULL || arrSize < 0)
		return (false);
	while (i < arrSize)
	{
		while (j < arrSize)
		{
			if (arr[i] == arr[j] * 2 && i != j)
				return (true);
			j++;
		}
		j = 0;
		i++;
	}
	return (false);
}

void printArray(int *arr, int arrSize)
{
	int i = 0;
	while (i < arrSize)
	{
		printf("%d ", arr[i]);
		i++;
	}
	printf("\n");
	return;
}

int main()
{
	int tst1[] = {10,2,5,3};
	int tst2[] = {3,1,7,11};
	int tst3[] = {-2,0,10,-19,4,6,-8};

	int size1 = sizeof(tst1) / sizeof(tst1[0]);
	int size2 = sizeof(tst2) / sizeof(tst2[0]);
	int size3 = sizeof(tst3) / sizeof(tst3[0]);

	printf("%d", checkIfExist (tst1, size1));
	printf("\n");
	printf("%d", checkIfExist (tst2, size2));
	printf("\n");
	printf("%d", checkIfExist (tst3, size3));
	printf("\n");
	return (0);
}
