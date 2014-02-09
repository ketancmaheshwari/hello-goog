# include<stdlib.h>
# include<stdio.h>

int main(){
  
  long double *now;
  long double new_mem;
  void create();

  now = (long double *)malloc (sizeof(new_mem));
  create(now);
  
  return 0;
}

void create(){
 printf("awesome stuff here\n");
}
