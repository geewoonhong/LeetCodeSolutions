/*
given int result, replace each element with the greatest element among
the elements to its right.
replace last element with -1
Note: The returned array must be malloced, assume caller calls free().
*/

 #include <stdio.h>
 #include <stdlib.h>

// int *replaceElements(int *arr, int arrSize, int *returnSize)
// {
// 	int i, j;
// 	int big;

// 	i = 0;
// 	big = 0;
// 	j = 1;
//     if (arr == NULL || arrSize == 0)
// 	{
//         *returnSize = 0;
//         return NULL;
//     }
//     int *result = (int *)malloc(arrSize * sizeof(int));
//     if (result == NULL)
// 	{
//         *returnSize = 0;
//         return NULL;
//     }
// 	while (i < arrSize - 1)
// 	{
// 		while (j < arrSize - 1)
// 		{
// 			if (arr[j] >= arr[j+1] && arr[j] >= big)
// 			{
// 				big = arr[j];
// 				j++;
// 			}
// 			else if (arr[j+1] > arr[j] && arr[j+1] >= big)
// 			{
// 				big = arr[j+1];
// 				j++;
// 			}
// 			else if(arr[j] < arr[j+1] && arr[j] < big)
// 				j++;
// 		}
// 		result[i] = big;
// 		big = 0;
// 		i++;
// 		if (i == arrSize -1)
// 			result[i] = arr[i+1];
// 		j = i + 1;
// 	}
// 	result[arrSize-1] = -1;
// 	*returnSize = arrSize;
// 	return (result);
// }

int *replaceElements(int *arr, int arrSize, int *returnSize)
{
	int RightMax = -1; // Start with -1 for the last element
    int i = arrSize - 1; // Start from the last element
    int *result = (int *)malloc(arrSize * sizeof(int));

    if (result == NULL)
	{
        *returnSize = 0;
        return NULL;
    }

    if (arr == NULL || arrSize == 0)
	{
        *returnSize = 0;
        return NULL;
    }

    while (i >= 0)
	{
        result[i] = RightMax; // Assign the greatest element to the right
        if (arr[i] > RightMax)
            RightMax = arr[i]; // Update the greatest element if necessary
        i--;
    }

    *returnSize = arrSize;
    return result;
}

int main()
{
    int arr[] = {17, 18, 5, 4, 6, 1};
    int arrSize = sizeof(arr) / sizeof(arr[0]);
    int returnSize;
    int *result = replaceElements(arr, arrSize, &returnSize);

    int i = 0;
    while (i < returnSize)
	{
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    free(result);
    return 0;
}
