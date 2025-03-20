#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/wait.h>
#include <time.h>

void sig_Handler(int sig)
{
    time_t curTime = time(NULL);
    printf("Active: Catched signal %s at %s",sig == SIGUSR1 ? "SIGUSR1" :
    "SIGUSR2", ctime(&curTime));
    signal(sig, SIG_DFL);    // востанавливаем старую диспозицию
}

int main()
{
    int pid,ppid;
    pid=getpid();
    ppid=getppid();

    signal(SIGUSR1, sig_Handler);    // перехватываем сигналы
    signal(SIGINT, SIG_DFL);         // ставим по умолчанию

    printf("Active: pid=%i ppid=%i\n", pid, ppid);
    int count = 0;
    while(1)
    {
        count++;
    }
    return 0;
}
