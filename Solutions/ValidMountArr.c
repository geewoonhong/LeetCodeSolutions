/*
int arr, return true iff it is a valid mountain array;

arr length >= 3;
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

*/

#include <stdio.h>
#include <stdbool.h>

bool validMountainArray(int* arr, int arrSize)
{
	int i = 1;
	int j = 0;

	if (arrSize < 3)
		return (false);
	while (i < arrSize -1)
	{
		if (arr[i] > arr[i-1] && arr[i] < arr[i+1])
			i++;
		else if(arr[i] > arr[i-1] && arr[i] > arr[i+1]) //mtn peak
			{
				j = i;
				while (j < arrSize -1)
				{
					if (arr[j] > arr[j+1])
						j++;
					else
						return (false);
				}
				return (true);
			}
		else
			break;
	}
	return (false);
}

int main()
{
	int tst1[] = {1,2,5,3};
	int tst2[] = {3,1,7,11};
	int tst3[] = {0,1,2,1,2};

	int size1 = sizeof(tst1) / sizeof(tst1[0]);
	int size2 = sizeof(tst2) / sizeof(tst2[0]);
	int size3 = sizeof(tst3) / sizeof(tst3[0]);

	printf("%d", validMountainArray(tst1, size1));
	printf("\n");
	printf("%d", validMountainArray(tst2, size2));
	printf("\n");
	printf("%d", validMountainArray(tst3, size3));
	printf("\n");
	return (0);
}
