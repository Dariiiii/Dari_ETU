 #include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <wait.h>
#include <string.h>
int main(int argc)
{
    int sid, pid, ppid, status;
    int pids[3];

    pid = getpid();
    ppid = getppid();

    printf("FATHER PARAMS: pid=%i ppid=%i \n", 
    pid,ppid);

    if((pids[0] = fork())==0) 
    {
        execl("son1","son1", NULL); 
    }
                                                                
    if((pids[1] = fork())==0) 
    {
        execl("son2","son2", NULL);
    }

    if((pids[2] = fork())==0) 
    {
        execl("son3","son3", NULL);  
    }

    system("ps xf -c > file1.txt");

    for(int i = 0; i < 3; i++)  // Посылаем сигнал SIGUSR1
        kill(pids[i], SIGUSR1);

    sleep(1);

    system("ps xf -c > file2.txt");

    for(int i = 0; i < 3; i++)  // Посылаем сигнал завершения
        kill(pids[i], SIGKILL);

}
