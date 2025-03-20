#include <sched.h>
#include <stdio.h>

int main (void) {
    struct sched_param shdprm;// значения параметров планирования
    int pid, pid1, pid2, pid3, ppid, status;
    int prPar = 50, pr1 = 50, pr2 = 50;

    pid = getpid();
    ppid = getppid();

    printf("FATHER PARAMS: pid=%ippid=%i\n", pid,ppid);
    shdprm.sched_priority = prPar;
        // меняем приоритет и политику планирования для род. процесса
    if (sched_setscheduler (0, SCHED_RR, &shdprm) == -1) {
        perror ("SCHED_SETSCHEDULER");
    }

    if((pid1=fork()) == 0)
    {
        shdprm.sched_priority = pr1;
        if (sched_setscheduler (pid1, SCHED_RR, &shdprm) == -1)
            perror ("SCHED_SETSCHEDULER_1");

        execl("son1", "son1", NULL);
    }

    if((pid2=fork()) == 0)
    {
        shdprm.sched_priority = pr2;
        if (sched_setscheduler (pid2, SCHED_RR, &shdprm) == -1)
            perror ("SCHED_SETSCHEDULER_2");
        execl("son2", "son2", NULL);
    }
    system("ps xf -Fc > proc.txt");

    return 0;
}