#include<stdio.h>
#include<omp.h>

void elemprod(double *c, double *a, double *b, int len){
    int i;
    #pragma omp parallel for
    for(i=0;i<len;i++){
        c[i] = a[i] * b[i];
        printf("%f, %f, %f\n", a[i],b[i],c[i]);
    } 
}


int main(int argc, char *argv[]){
    double v1[10] = {1,2,3,4,5,6,7,8,9,10};
    double v2[10] = {1,2,3,4,5,6,7,8,9,10};
    double v3[10];
    elemprod(v3, v1, v2, 10);
    int j;
    for (j=0;j<10;j++)
        printf("%f\n", v3[j]);
    
    return 0;
}
