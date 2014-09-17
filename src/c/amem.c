# include<stdlib.h>
# include<stdio.h>
# include "amem.h"

int main(){
  
  long double *now;
  long double new_mem;

  now = (long double *)malloc (sizeof(new_mem));
  create(now);
  
  return 0;
}

void create(){
 printf("some stuff here\n");
}
