 #include <stdlib.h>
 #include <string.h> 
 #include <stdio.h>

char** fizzBuzz(int n, int* returnSize) {

    char **answer = (char **)calloc(n, sizeof(char *)); //works
    // char **answer = (char **)calloc(n, sizeof(char)); //breaks 
    if (answer == NULL) return NULL;
    for (int i = 0; i < n; i++)
    {
        answer[i] = (char *)calloc(10, sizeof(char));//allocate each element 
        if (answer[i] == NULL) return NULL;
    }
    for (int i = 0; i < n; i++) {
        if (returnSize[i] % 3 == 0 && returnSize[i] % 5 == 0)
            strcpy(answer[i], "FizzBuzz");
        else if (returnSize[i] %3==0) 
            strcpy(answer[i], "Fizz");
        else if (returnSize[i] %5==0) 
            strcpy(answer[i], "Buzz");
        else 
            // answer[i] = (returnSize[i] + '0');
            sprintf(answer[i], "%d", returnSize[i]);
    }
    return answer;
}

int main (void)
{
    int n = 3;
    int num_array[3] = {15, 3, 5};
    char **fb_array = fizzBuzz(n, num_array);
    
    if (fb_array != NULL)
    {
        for (int i = 0; i < n; i++)
        {
            printf("%s\n", fb_array[i]);
            free(fb_array[i]);
        }
        free(fb_array);
    }
    return 0;
}
