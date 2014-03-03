/* Include header files */
#include <stdio.h>
#include <stdlib.h>

/* create structure */
struct node {
    int item;
    struct node* prev;
    struct node* next;  
};

/* start main */
int main(void){

void create(struct node* p);
int count(struct node* p);
void print(struct node* p);

int numitems;

struct node* head;
printf ("Test\n");
head = (struct node *)malloc(sizeof(struct node));
create(head);
print(head);
numitems = count(head);
printf("\nThere are %d items in the list\n", numitems);

return 0;
}

void create(struct node* list){
    printf("Input a number (-999 at end):\n");
    scanf("%d", &list->item);

    if (list->item == -999){
        list -> next = NULL;
    }
    else{
        list->next = (struct node *)malloc (sizeof(struct node));
        create(list->next); /* recursive call to create */
    }
    return;
}

void print(struct node* list){
    if (list -> next != NULL){
        printf("%d ", list->item);
        if (list -> next -> next == NULL){
            printf("%d ", list -> next -> item);
        }
        print (list -> next);
}
return;
}

int count(struct node* list){
    if (list -> next == NULL)
        return (0);
    else
        return (1+count(list -> next));
}
