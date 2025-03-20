#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

int main()
{
    int pid,ppid;
    pid=getpid();
    ppid=getppid();
    printf("SON_2 PARAMS: pid=%i ppid=%i\n", pid,
    ppid);
    signal(SIGUSR1, SIG_IGN); // игнорируем сигнал
    while(1) 
        pause();
    return 0;
}
