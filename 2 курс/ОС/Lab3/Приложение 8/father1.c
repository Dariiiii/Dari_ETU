#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sched.h>

int main()
{
    int pid1 = 0, pid2 = 0;
    int all = 200;
    int index_out = 0; 

    if ((pid1 = fork()) == 0) // потомок
    {
        for (int index1 = 0; index1 < 200; index1++) {
            printf("Child 1: i = %d, pid = %d, ppid = %d\n", index1, getpid(), getppid());
            index_out++;
        }

        printf("Завершение процесса 1\n");
        exit(0);
    }
    if ((pid2 = fork()) == 0 && pid1 > 0) // потомок
    {
        for (int index2 = 0; index2 < 200; index2++) {
            printf("Child 2: i = %d, pid = %d, ppid = %d\n", index2, getpid(), getppid());
            index_out++;
        }

        printf("Завершение процесса 2\n");
        exit(0);
    }
    else                    // родитель
    {
        for (int index3 = 0; index3 < 200; index3++) {
            printf("Parent: i = %d, pid = %d, ppid = %d\n", index3, getpid(), getppid());
            index_out++;
        }
    }
    
    system("ps xf -Fc > proc.txt");

    printf("Завершение процесса\n");
    exit(1);
}
