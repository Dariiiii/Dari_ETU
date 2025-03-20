#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <time.h>

int cmp(const void*a, const void*b){
    return *(int*)a - *(int*)b;
}

void bsort(int *arr, int arr_size){
    bool sorted = false;
    while(!sorted){
        sorted = true;
        for(int i=0; i < arr_size-1; i++){
            if (arr[i]>arr[i+1]){
                sorted = false;
                int k = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = k;
            }
        }
    }
}

int main()
{
    //int arr[1000];
    int qsorted[1000];
    int bsorted[1000];
    for(int i=0; i<1000; i++){
        int h;
        scanf("%d ", &h);
        //arr[i] = h;
        qsorted[i] = h;
        bsorted[i] = h;
    }

    clock_t start = clock();
    bsort(bsorted, 1000);
    clock_t end = clock();

    float btime = (float)(end - start)/CLOCKS_PER_SEC;

    start = clock();
    qsort(qsorted, 1000, sizeof(int), cmp);
    end = clock();

    float qtime = (float)(end - start)/CLOCKS_PER_SEC;

    for(int i=0; i<1000; i++){
        printf("%d ", bsorted[i]);
    }
    printf("\n%f", btime);
    printf("\n%f ", qtime);

    return 0;
}