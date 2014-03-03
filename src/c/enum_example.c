# include<stdlib.h>
# include<stdio.h>

int main(){
    typedef enum {
        NORTH,
        EAST,
        WEST,
        SOUTH
    }directions;
    directions a, b, c, d;
    a=EAST;
    b=WEST;
    printf ("%d, %d\n", a, b);
  
  return 0;
}

