# include<stdlib.h>
# include<stdio.h>

int main(){
  
  long double *now;
  long double new_mem;
  void create(long double*);

  now = (long double *)malloc (sizeof(new_mem));
  create(now);
  
  return 0;
}

void create(long double * anow){
 printf("awesome stuff here\n");
}
