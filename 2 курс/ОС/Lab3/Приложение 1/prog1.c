#include <stdio.h>
#include <math.h>
#include <sys/resource.h>
#include <stdlib.h>

// Пример с однократным вычислением для каждого процесса
void main(int argc, char* argv[])
{
    int m, n, all, pid;
    m=5000;         // Счетчик для родительского процесса
    n=1;            // Счетчик для дочернего процесса
    pid = fork();   // Создаем дочерний процесс
    if(pid == -1)
    {
        perror("fork error");
        exit(1);
    }
    printf("\npid=%i\n",pid);
    if(pid != 0)    // если родитель
    {
        for(int j = 1; j <= 1000; j++)
        {
            m-=1;
        }
        printf("родитель: %i\n",m);
    }
    else {          // если потомок (pid == 0)
        for(int i = 1; i <= 1000; i++)
        {
            n+=1;
        }
        printf("потомок: %d\n",n);
    }

    printf("Программа завершена\n");
    exit(1);
}
