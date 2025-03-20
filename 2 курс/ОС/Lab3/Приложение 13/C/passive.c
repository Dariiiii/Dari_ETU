#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <time.h>
#include <unistd.h>

void sig_Handler(int sig)
{
    time_t curTime = time(NULL);
    printf("Passive: Catched signal %s at %s",sig == SIGUSR1 ? "SIGUSR1" :
    "SIGUSR2", ctime(&curTime));
    signal(sig, SIG_DFL);    // востанавливаем старую диспозицию
    pause();
}

int main()
{
    int pid,ppid;
    pid=getpid();
    ppid=getppid();

    signal(SIGUSR1,sig_Handler); // перехватываем сигналы
    signal(SIGINT,SIG_DFL);         // ставим по умолчанию

    printf("Passive: pid=%i ppid=%i\n", pid, ppid);
    
    pause();

    return 0;
}
