 #include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <wait.h>
#include <string.h>
int main(int argc, char *argv[])
{
    int sid, pid, pid1, ppid, status;
    char command[50];
    if (argc < 2)
        return -1;

    pid = getpid();
    ppid = getppid();
    sid = getsid(pid);

    sprintf(command, "ps xjf | grep \"STAT\\|%d\" > %s", 
    sid, argv[1]);  // команда для записи статистики в выходной файл
    printf("FATHER PARAMS: sid = %i pid=%i ppid=%i \n", 
    sid, pid,ppid);

    if((pid1=fork())==0) execl("son1","son1", NULL); // потомок, которого родительский 
                                                                // процесс будет дожидаться
    if(fork()==0) execl("son2","son2", argv[1], NULL); // родитель не будет дожидаться завершения

    if(fork()==0) execl("son3","son3", NULL);   // как и в прошлом варианте, но потомок
                                                          // успеет завершиться раньше родителя 
    system(command);
    waitpid(pid1, &status, WNOHANG); //эта строка исключается в п.б) и в)
}
