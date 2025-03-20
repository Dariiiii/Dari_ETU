#include <stdio.h>
#include <sys/types.h>
#include <wait.h>

int main()
{
    char *args[] = {"son2", "-l", "-p", NULL};  // список аргументов
    char *envp[] = {"SHELL=/usr/bin/bash", "USER=testuser", NULL};           // аргументы окружения
    int status, result;
    int pid[4];
    pid[0] = getpid();
    int ppid = getppid();
    printf("FATHER PARAM: pid=%i ppid=%i\n", pid[0], ppid);

    if((pid[1] = fork()) == 0)
        execl("son1", "son1", (char *) NULL);
    if((pid[2] = fork()) == 0)
        execv("son2", args);
    if((pid[3] = fork()) == 0)
        execle("son3", "-t", "-r", NULL, envp);

    system("ps xf > file.txt");
    for (int i = 1; i < 4; i++)
    {
        result = waitpid(pid[i], &status, WUNTRACED);
        printf("\n%d) Child proccess with pid = %d is finished with status %d\n", i,
        result, status);
    }
    return 0;
}
