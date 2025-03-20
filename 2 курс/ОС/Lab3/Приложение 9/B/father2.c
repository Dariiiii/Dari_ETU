#include <sched.h>
#include <stdio.h>
#include <unistd.h>

int main (void) {
    struct sched_param shdprm;// значения параметров планирования
    int pid, pid1, pid2, pid3, ppid, status;
    int prPar = 50, pr1 = 60, pr2 = 10, pr3 = 4;
    int a = 50, b = 60, prod = 0;

    pid = getpid();
    ppid = getppid();

    printf("FATHER PARAMS: pid=%ippid=%i\n", pid,ppid);
    shdprm.sched_priority = prPar;
        // меняем приоритет и политику планирования для род. процесса
    if (sched_setscheduler (0, SCHED_FIFO, &shdprm) == -1) {
        perror ("SCHED_SETSCHEDULER");
    }

    if((pid1=fork()) == 0)
    {
        shdprm.sched_priority = pr1;
        if (sched_setscheduler (pid1, SCHED_FIFO, &shdprm) == -1)
            perror ("SCHED_SETSCHEDULER_1");

        execl("son1", "son1", NULL);
    }

    if((pid2=fork()) == 0 && pid1 > 0)
    {
        shdprm.sched_priority = pr2;
        if (sched_setscheduler (pid2, SCHED_FIFO, &shdprm) == -1)
            perror ("SCHED_SETSCHEDULER_2");
        execl("son2", "son2", NULL);
    }
    if((pid3=fork()) == 0 && pid2 > 0)
    {
        shdprm.sched_priority = pr3;
        if (sched_setscheduler (pid3, SCHED_FIFO, &shdprm) == -1)
            perror ("SCHED_SETSCHEDULER_2");
        execl("son3", "son3", NULL);
    }
    else {
        for(int index = 0; index < 400; index++)
        {
            prod = a * b;
        }
    }


    system("ps -o f,s,pid,ppid,cls,pri,ni,stat,cmd,rtprio xf > proc.txt");

    printf("Процесс с pid = %d завершен\n", wait(&status));
    printf("Процесс с pid = %d завершен\n", wait(&status));
    printf("Процесс с pid = %d завершен\n", wait(&status));

    return 0;
}