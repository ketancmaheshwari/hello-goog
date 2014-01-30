#include<stdio.h>
#include "mpi.h"

int main(int argc, char *argv[]){

    int rc, num_tasks , my_rank;

    rc = MPI_Init( &argc, &argv);
    
    if (rc != MPI_SUCCESS) {
        fprintf( stderr, "Unable to set up MPI");
        MPI_Abort( MPI_COMM_WORLD , rc);
    }
    
    MPI_Comm_size(MPI_COMM_WORLD, &num_tasks);
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

    MPI_Finalize ();
    return 0;
}
