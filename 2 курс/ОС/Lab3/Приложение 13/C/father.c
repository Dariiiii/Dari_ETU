#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <wait.h>
#include <string.h>
#include <time.h>

int main(int argc)
{
    int sid, pid, ppid, status;
    int pids[2];
    char *sons[2] = {"active", "passive"};
    time_t curTime = time(NULL);

    pid = getpid();
    ppid = getppid();

    printf("FATHER PARAMS: pid=%i ppid=%i \n", 
    pid,ppid);

    if((pids[0] = fork()) == 0)
        execl("active", "active", NULL);

    if((pids[1] = fork()) == 0)
        execl("passive", "passive", NULL);

    system("ps -o f,s,pid,ppid,cls,pri,ni,stat,cmd,rtprio xf > file1.txt");

    for(int i = 0; i < 2; i++) {

        kill( pids[i], SIGUSR1);

        curTime = time(NULL);

        printf("SIGUSR1 has been sent to %s process at %s", sons[i], ctime(&curTime));
    }   

    system("ps -o f,s,pid,ppid,cls,pri,ni,stat,cmd,rtprio xf > file2.txt");

    for(int i = 0; i < 3; i++)  // Посылаем сигнал завершения
        kill(pids[i], SIGKILL);

    system("ps -o f,s,pid,ppid,cls,pri,ni,stat,cmd,rtprio xf > file3.txt");
}
