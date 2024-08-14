/*
given a fixed-length arr, 
duplicate each occurence of 0,
shift remaining elements to the right
arr[1] = 0; arr[1+1] = 0; count starts from arr[1+2]
do not increase array length; that stays the same
*/
#include <unistd.h>


void duplicateZeros(int *arr, int arrSize) {
    for (int i=0;i<arrSize;i++) //to check throught the arr
    {
        if (arr[i]==0) //if val at i == 0
        {
            int j = arrSize-2;
            while (j >= i)
            {
                arr[j+1] = arr[j];
                j--;
            }
            i++; //skip duplicate
        }
    }
    for (int i=0;i<arrSize;i++)
        printf("%d, ", arr[i]);
    return;
}

int main (void)
{
    int arr[] = {1,0,2,3};
    int arrSize = 4;
    duplicateZeros(arr, arrSize);
    return 0;
}