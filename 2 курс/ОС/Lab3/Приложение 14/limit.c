#include <stdio.h>
#include <sys/time.h>
#include <sys/resource.h>
void main()
{
    int pr, pid, i;
    pid=getpid();
    for (i = -100; i < 1; i++)
    {
        setpriority(PRIO_PROCESS, pid, i);
        pr = getpriority(PRIO_PROCESS, pid);
    if (pr != i) continue;
    else
    {
        printf("Нижняя граница = %d\n", pr);
        printf("Запросили %d, получили %d\n", i, pr);
        break;
    }
    }
    for (i = 1; i < 100; i++)
    {
        setpriority(PRIO_PROCESS, pid, i);
        pr = getpriority(PRIO_PROCESS, pid);
        if (pr == i) continue;
        else
        {
            printf("Верхняя граница = %d\n", pr);
            printf("Запросили %d, получили %d\n", i, pr);
            break;
        }
    }
}