#include<stdio.h>

__global__ void hellocuda(int* tidx ){
   /* *tidx = 100; */
   int x = threadIdx.x;
   tidx[x]=threadIdx.x;
}

int main(){
    
    int i;
    int * d_tidx;

    int * h_tidx;
    
    cudaError_t err = cudaMalloc((void**) &d_tidx, 20*sizeof(int));
    if (err != cudaSuccess){
        printf("%s on %s at line %d\n", cudaGetErrorString(err), __FILE__, __LINE__);
        exit(EXIT_FAILURE);
    }

    h_tidx=(int *)malloc(20*sizeof(int));

    hellocuda<<<200,20,20>>>(d_tidx);
    
    cudaMemcpy(h_tidx, d_tidx, 20*sizeof(int), cudaMemcpyDeviceToHost);

    for (i=0; i<20;i++)
        printf("Thread index: %d\n", h_tidx[i]);
    
    /*
    printf("Number of Blocks (Grid dim): %d\n", *h_gdim);
    printf("Number of Threads in current block (Block dim): %d\n", *h_bdim);
    printf("Block index: %d\n", *h_bidx);
    printf("Thread index: %d\n", *h_tidx);
    */
    return EXIT_SUCCESS;
}
