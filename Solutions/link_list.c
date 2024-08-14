#include <stdio.h>
#include <stdlib.h> // Include necessary headers

// Definition for singly-linked list
struct ListNode {
    int val;
    struct ListNode *next;
};

// Function prototype
struct ListNode* middleNode(struct ListNode* head)
{
    int steps = 0;
    int i = 0;
    struct ListNode* temp = head;
    while (temp != NULL) // going through the list 
    {
        temp = temp -> next; // head becomes the next node in list
        steps++; // number of nodes
    }
    while(i != (steps/2)) {
        head = head -> next;
        i++; //number of moves
    }
    return (head);
}

int main() {
    // Create sample linked list nodes
    struct ListNode* node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node4 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node5 = (struct ListNode*)malloc(sizeof(struct ListNode));

    // Initialize node values
    node1->val = 1;
    node2->val = 2;
    node3->val = 3;
    node4->val = 4;
    node5->val = 5;

    // Link nodes together
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    node5->next = NULL; // Mark end of the list

    // Call the middleNode function
    struct ListNode* middle = middleNode(node1);

    // Print the value of the middle node
    printf("Value of the middle node: %d\n", middle->val);

    // Free dynamically allocated memory
    free(node1);
    free(node2);
    free(node3);
    free(node4);
    free(node5);

    return 0;
}
