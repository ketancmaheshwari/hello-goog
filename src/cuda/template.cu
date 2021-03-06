#include <stdio.h>
#include <stdlib.h>
#include<cuda.h>

__global__ void func(int *t1) {
    int i=blockDim.x * blockIdx.x + threadIdx.x;
    int j=threadIdx.x;
    t1[i]=j;
}

int main() {
    int *d_t1;
    int *h_t1;
    int i=0;
    
    size_t size = N*sizeof(float);
    
    //Memory allocation
    cudaError_t err = cudaMalloc((void **)&d_t1, size);
    if (err != cudaSuccess){
        printf("%s on %s at line %d\n", cudaGetErrorString(err), __FILE__, __LINE__);
        exit(EXIT_FAILURE);
    }
    h_t1=(int *)malloc(size);
    
    //Initialize the array
    for (i=0; i<N; i++)
        h_t1[i] = 0;

    //Run invoke threads to execute the kernel
    cudaMemcpy(d_t1, h_t1, size, cudaMemcpyHostToDevice);
    thread_multi<<<4,N/4>>>(d_t1);
    cudaMemcpy(h_t1, d_t1, size, cudaMemcpyDeviceToHost);

    for(i=0; i<N; i++)
        printf("%d: %d\n",i, h_t1[i]);

    cudaFree(d_t1);
    free(h_t1);
    printf("\nDone\n");

    return 0;
}

