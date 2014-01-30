#include <stdio.h>
#include <omp.h>

int main(int argc, char *argv[]){

   printf("Hello from master thread.\n");

#pragma omp parallel
   {
      printf("Team member %d reporting from team of %d\n",
             omp_get_thread_num(), omp_get_num_threads() );
   }

   printf("Master thread finished, goodbye.\n");
}
