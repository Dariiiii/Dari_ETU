#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void sigHandler(int sig)
{
    printf("SON_3: Сигнал SIGUSR1 %d был получен\n", sig);
    signal(sig,SIG_DFL); // востанавливаем старую диспозицию
}
int main()
{
    int pid,ppid;
    pid=getpid();
    ppid=getppid();
    signal(SIGUSR1, sigHandler);
    printf("SON_3 PARAMS: pid=%i ppid=%i\n", pid,
    ppid);
    while(1) 
        pause();
    return 0;
}
