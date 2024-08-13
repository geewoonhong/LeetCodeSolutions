/*

given an int array heights that are in a random order
sort to a non-decreasing order int arrary expected[i]
and return # of indices where
heights[i] != expected[i]

example:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

*/
#include <stdlib.h>
#include <stdio.h>

int	heightChecker(int *heights, int heightsSize)
{
	int i = 0;
	int j = 0;
	int box = 0;
	int k = 0;
	int *res;

	res = malloc(heightsSize * sizeof(int));
	while (i < heightsSize)
	{
		res[i] = heights[i];
		i++;
	}
	i = 0;
	while (i < heightsSize)
	{
		while (j < heightsSize - 1)
		{
			if (res[j] > res[j+1])
				{
					box = res[j+1];
					res[j+1] = res[j];
					res[j] = box;
				}
			j++;
		}
		j = 0;
		i++;
	}
	i = 0;
	while (i < heightsSize)
	{
		if (heights[i] != res[i])
			k++;
		i++;
	}
	free(res);
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

int main()
{
	int tst1[] = {1,1,4,2,1,3};
	int tst2[] = {5,1,2,3,4};
	int tst3[] = {1,3,2,4};

	int size1 = sizeof(tst1) / sizeof(tst1[0]);
	int size2 = sizeof(tst2) / sizeof(tst2[0]);
	int size3 = sizeof(tst3) / sizeof(tst3[0]);

	int res1 = heightChecker(tst1, size1);
	int res2 = heightChecker(tst2, size2);
	int res3 = heightChecker(tst3, size3);

	printf("Num of different indices for tst1: %d\n", res1);
	printf("Num of different indices for tst2: %d\n", res2);
	printf("Num of different indices for tst3: %d\n", res3);
    return (0);
}
