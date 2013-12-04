/* Include header files */
#include <stdio.h>
#include <stdlib.h>

/* create structure */
struct node {
    int item;
    struct node* prev;
    struct node* next;  
};
typedef struct node node;

/* start main */
int main(void){

node* head;
printf ("Test\n");

/* allocate memory to a node */
node* firstnode = (node *)malloc (sizeof(node));
node* secondnode = (node *)malloc (sizeof(node));
firstnode -> item = 100;
firstnode -> prev = head;
firstnode -> next = secondnode;

secondnode -> item = 200;
secondnode -> prev = firstnode;
secondnode -> next = NULL;

/* Test */
printf ("%d\n", firstnode -> next -> item);

return 0;
}

