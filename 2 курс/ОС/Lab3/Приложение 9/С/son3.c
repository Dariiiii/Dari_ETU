#include <stdio.h>
#include <stdlib.h>
#include <sched.h>
#include <time.h>

#define BILLION  1000000000.0

int main()
{
    struct timespec start, end;
    clock_gettime(CLOCK_REALTIME, &start);
    struct sched_param shdprm;
    int i, pid, ppid, a = 100, b = 50, prod = 0;
    pid=getpid();
    ppid=getppid();

    printf("SON_3 PARAMS: pid=%i ppid=%i\n",pid,ppid);
    printf ("SON_3: Текущая политика планирования для текущего процесса: ");
    switch (sched_getscheduler (0))
    {
        case SCHED_FIFO:
            printf ("SCHED_FIFO\n");
            break;
        case SCHED_RR:
            printf ("SCHED_RR\n");
            break;
        case SCHED_OTHER:
            printf ("SCHED_OTHER\n");
            break;
        case -1:
            perror ("SCHED_GETSCHEDULER");
            break;
        default:
            printf ("Неизвестная политика планирования\n");
    }
    if (sched_getparam (0, &shdprm) == 0)
        printf ("SON_3: Текущий приоритет текущего процесса: %d\n", shdprm.sched_priority);
    else
        perror ("SCHED_GETPARAM");
    
    for(int index = 0; index < 400; index++)
    {
        prod = a * b;
    }

    clock_gettime(CLOCK_REALTIME, &end);
    double time_spent = (end.tv_sec - start.tv_sec) +
                        (end.tv_nsec - start.tv_nsec) / BILLION;
 
    printf("son3 завершен\n");
    printf("Время выполнения son3 - %f seconds\n", time_spent);
    return 0;
}