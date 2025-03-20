#include <stdio.h>
#include <sys/mman.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <stdlib.h>
#include <unistd.h>


int main (void)
{
    int i, pid, ppid, status;
    int prior = -5, pr; // величина приоритета 

    pid = getpid();
    ppid = getppid();

    // setpriority(PRIO_PROCESS, pid, prior);  // задаем приооитет родителю
    // if((pr = getpriority(PRIO_PROCESS, pid)) != prior)
    //     perror("SETPRIORITY");

    printf("father params: pid = %i ppid = %i priority = %i\n",
    pid,ppid,pr);

    for (i = 0; i < 2; i++) // запустим два потомка
        if(fork() == 0)
        {
            execl("son", "son", NULL);
        }

    system("ps -o f,s,pid,ppid,cls,pri,ni,stat,cmd,rtprio xf > proc.txt");
    for (i = 0; i < 2; i++)
        printf("Процесс с pid = %d завершен\n", wait(&status));
    return 0;
}