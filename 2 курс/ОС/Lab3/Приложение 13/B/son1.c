#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

int main()
{
    int pid,ppid;
    pid=getpid();
    ppid=getppid();
    printf("SON_1 PARAMS: pid=%i ppid=%i\n", pid,
    ppid);

    signal(SIGUSR1, SIG_DFL); // выполняем действие по умолчанию
    while(1) 
        pause();
    return 0;
}
