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

void create(node* p);
int count(node* p);
void print(node* p);

int numitems;

node* head;
printf ("Test\n");
head = (node *)malloc(sizeof(node));
create(head);
print(head);
numitems = count(head);
printf("\nThere are %d items in the list\n", numitems);

return 0;
}

void create(node* list){
    printf("Input a number (-999 at end):\n");
    scanf("%d", &list->item);

    if (list->item == -999){
        list -> next = NULL;
    }
    else{
        list->next = (node *)malloc (sizeof(node));
        create(list->next); /* recursive call to create */
    }
    return;
}

void print(node* list){
    if (list -> next != NULL){
        printf("%d ", list->item);
        if (list -> next -> next == NULL){
            printf("%d ", list -> next -> item);
        }
        print (list -> next);
}
return;
}

int count(node* list){
    if (list -> next == NULL)
        return (0);
    else
        return (1+count(list -> next));
}
