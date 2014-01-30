#include<stdio.h>
#include <omp.h>

int main(){
    
    const int num_steps = 100000; 
    double x, sum = 0.0; 
    const double step = 1.0/(double)num_steps; 
    int i;
    #pragma omp parallel for reduction(+:sum) private(x) 
    for (i=1; i<= num_steps; i++){ 
        x = (double)(i-0.5)*step; 
        sum += 4.0/(1.0+x*x); 
    } 
    const double pi = step * sum;
    printf("The value if pi is %f\n", pi);
}
