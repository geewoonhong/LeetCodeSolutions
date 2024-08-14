#include <stdio.h>
#include <stdbool.h>

int maximumWealth(int **accounts, int accountsSize, int *accountsColSize) {
	int i = 0;
	int j = 0;
	int wealth [4] = {0};
	int *temp;
	bool swap;

	while(i < accountsSize) {
		while (j < *accountsColSize) {
			wealth[i] += accounts[i][j];
			j++;
		}
		j = 0;
		i++;
	}
	i = 0;
	j = 0;
	while (i < accountsSize - 1) {
		swap = false;
		j = 0;
		while (i < accountsSize - i - 1) {
			if (wealth[j] > wealth[j+1]) {
				temp = &wealth[j];
				wealth[j] = wealth[j +1];
				wealth[j+1] = *temp;
				swap = true;
				j++;
			}
			if (swap == false)
				break;
		}
		j = 0;
		i++;
	}
	return (wealth[accountsSize -1]);
}

int main(void) {
	int accounts[3][2] = {
		{1, 5},
		{7, 3},
		{3, 5},
	};
	int size = 3;
	int result = maximumWealth(*accounts, size, accounts[0]);
	printf("%d\n", result);
	return (0);
}
