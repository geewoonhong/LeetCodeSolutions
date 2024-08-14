#include <stdlib.h>
#include <stdio.h>

int* sortedSquares(int* nums, int numsSize) {
    int *r;
    r = calloc(numsSize, sizeof(int *));
    for (int i = 0; i < numsSize; i++)
        r[i] = nums[i] * nums[i]; //square of each num
    int i =0;
    int j = 0;
    int temp =0;
    while (i < numsSize)
    {
        j =0;
        while (j < numsSize-i-1)
        {
            if (r[j] > r[j+1])
            {
                temp = r[j];
                r[j] = r[j+1];
                r[j+1] = temp;
            }
            j++;
        }
        i++;
    }
    return r;   
}

int main(void)
{
    int nums[5] = {4,1,0,3,10};
    int *r = sortedSquares(nums, 5);
    int i =0;
    while (i<5) {
        printf("%d, ", r[i]);
        i++;
    }
    free(r);
    return 0;
}


/* int *returnSize ... what could it be? 
*/
// int* sortedSquares(int* nums, int numsSize, int* returnSize) {
//     int *r;
//     *returnSize = numsSize; //why is this line necessary?
//     r = calloc(numsSize, sizeof(int *));
//     for (int i = 0; i < numsSize; i++)
//         r[i] = nums[i] * nums[i]; //square of each num
//     int i =0;
//     int j = 0;
//     int temp =0;
//     while (i < numsSize)
//     {
//         j =0;
//         while (j < numsSize-i-1)
//         {
//             if (r[j] > r[j+1])
//             {
//                 temp = r[j];
//                 r[j] = r[j+1];
//                 r[j+1] = temp;
//             }
//             j++;
//         }
//         i++;
//     }
//     return r;   
// }

// int main(void)
// {
//     int nums[5] = {4,1,0,3,10};
//     int a = 5;
//     int *returnSize = &a;
//     int *r = sortedSquares(nums, 5, returnSize);
//     int i =0;
//     while (i<5) {
//         printf("%d, ", r[i]);
//         i++;
//     }
//     free(r);
//     return 0;
// }

