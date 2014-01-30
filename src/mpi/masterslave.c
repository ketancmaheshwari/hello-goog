#include "mpi.h"
#include <stdio.h>

void master(int rank){
    printf("I am master and my rank is %d.\n", rank);
}

void slave(int rank){
    printf("I am slave and my rank is %d.\n", rank);
}

int main(int argc, char **argv){

    int myrank;
    int size;

    MPI_Init(&argc, &argv);

    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    
    if(myrank == 0){
        master(myrank);
        printf("In total, we're %d processes.\n", size);
    } else
        slave(myrank);

    MPI_Finalize();
    return 0;
}
