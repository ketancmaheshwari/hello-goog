#include <stdio.h>

void swap (int *a, int *b){
    int tmp;
    tmp=*a;
    *a=*b;
    *b=tmp;
}

int main(void){

    int x=100;
    int y=200;
    printf("Befor swap: x=%d and y=%d\n", x, y);
    swap(&x, &y);
    printf("After swap: x=%d and y=%d\n", x, y);

    return 0;
}
