#include <stdio.h>

int main(int argc, char *argv[]){
    
    int *d_a=0, *h_a=0;
    int dimx = 16;
    int i;
    int allocsize = dimx * sizeof(int);

    h_a = (int *)malloc(allocsize);

    cudaMalloc((void **) &d_a, allocsize);

    if (d_a == 0 || h_a == 0){
        printf("Memory allocation error!");
        return 1;
    }

    cudaMemset(d_a, 0, allocsize);

    cudaMemcpy(h_a, d_a, allocsize, cudaMemcpyDeviceToHost);

    for (i=0;i < dimx; i++)
        printf("%d ", h_a[i]);
    printf("\n");

    free(h_a);
    cudaFree(d_a);

    return 0;
}
