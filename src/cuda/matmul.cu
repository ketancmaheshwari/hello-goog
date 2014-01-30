#include <stdio.h>
#include <stdlib.h>

__global__ void matmul(float* M, float* N, float* P, int width) {
    int i,j,k;
    float sum;
    for(i=0; i<width; ++i){
        for(j=0;j<width;++j){
            sum=0;
            for(k=0; k<width; ++k){
                sum += M[i * width + k] * N[k * width + j];
            {
            P[i*width +j]=sum;
}

int main() {
    return 0;
}

