/* 
Divide number by 10 again and again 
*/

#include <stdio.h>

int findNumbers(int* nums, int numsSize) {
    int nb;
    int r = 0;
    for (int i = 0; i < numsSize; i++) 
    {
        int count = 1;
        nb = nums[i]; 
        while (nb > 9)
        {
            nb = nb/10;
            count++;
        }
        if (count%2 == 0) //if nums[i] is even nb of digits
        {
         r++;
        }
    }
    return r;
}

int main(void)
{
    int nums[5] = {12, 34, 2, 6, 7866};
    int r;
    r = findNumbers(nums,5);
    printf("%d\n", r);
    return 0;
}