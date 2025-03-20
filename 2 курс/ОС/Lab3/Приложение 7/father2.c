#include <stdio.h>
#include <sys/types.h>
#include <wait.h>
#include <string.h>

int main()
{
    int i, ppid, pid[4], status[3], result[3];
    char *son[] = {"son1", "son2", "son3"};
    int option[] = {WNOHANG, WNOHANG, WNOHANG}; // комбинация констант
     
    pid[3] = getpid();
    ppid = getppid();

    printf("FATHER PARAMS: pid=%i ppid=%i\n", pid[3],ppid);

    for (i = 0; i < 3; i++)
        if((pid[i] = fork()) == 0)  // создаем три дочерних процесса
            execl(son[i], son[i], NULL);
    system("ps -o f,s,pid,ppid,cls,pri,ni,stat,cmd,rtprio xf > proc.txt");

    for (i = 0; i < 3; i++)
    {                           // отслеживаем из в зависимости от опций
        result[i] = waitpid(pid[i], &status[i], option[i]);
        printf("%d) Child with pid = %d is finished with status %d\n", (1 + i), result[i], status[i]);
    }


    for (i = 0; i < 3; i++)
    {
        if(WIFEXITED(status[i] == 0))   // проверяем возвращаемый код завершения
            printf("Proccess pid = %d was failed.\n", pid[i]);
        else
            printf("Proccess pid = %d was success.\n", pid[i]);
    }
    return 0;
}
