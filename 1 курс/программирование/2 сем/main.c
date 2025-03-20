#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <time.h>

void bub_sort(int *arr){
    bool flag = false;
    while(!flag){
        flag = true;
        for(int i=0; i < 1000-1; i++){
            if (arr[i]>arr[i+1]){
                flag = false;
                int a = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = a;
            }
        }
    }
}

int cmp(const void*a, const void*b){
    return *(int*)a - *(int*)b;
}

int main()
{
    int q_sorted[1000];
    int bub_sorted[1000];
    for(int i=0; i<1000; i++){
        int a;
        scanf("%d ", &a);
        q_sorted[i] = a;
        bub_sorted[i] = a;
    }

    clock_t q_start = clock();
    qsort(q_sorted, 1000, sizeof(int), cmp);
    clock_t q_end = clock();

    float q_time = (float)(q_end - q_start)/CLOCKS_PER_SEC;

    clock_t b_start = clock();
    bub_sort(bub_sorted);
    clock_t b_end = clock();

    float bub_time = (float)(b_end - b_start)/CLOCKS_PER_SEC;

    for(int i=0; i<1000; i++){
        printf("%d ", bub_sorted[i]);
    }
    printf("\n%f", bub_time);
    printf("\n%f ", q_time);

    return 0;
}