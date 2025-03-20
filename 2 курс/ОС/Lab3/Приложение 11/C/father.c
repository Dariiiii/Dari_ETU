#include <stdio.h>
#include <sched.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main (void)
{
    int i, pid, ppid, status;
    int fdrd, fdwr;
    char c;
    struct sched_param shdprm;

    if (mlockall((MCL_CURRENT | MCL_FUTURE)) < 0)
        perror("mlockall error");

    pid = getpid();
    ppid = getppid();
    shdprm.sched_priority = 1;  // меняем политику планирования
    if (sched_setscheduler (0, SCHED_RR, &shdprm) == -1)
        perror ("SCHED_SETSCHEDULER_1");

    if ((fdrd = open("infile.txt",O_RDONLY)) == -1) // открываем файл 
        perror("Openning file");                              // только для чтения
    if ((fdwr = creat("outfile.txt",00666)) == -1)   // создаем файл
        perror("Creating file");                             // с rw- разрешением

    printf("file read decriptor = %d\n", fdrd);
    printf("file write decriptor = %d\n", fdwr);
    for (i = 0; i < 2; i++) // запустим два потомка
        if(fork() == 0)
        {
            shdprm.sched_priority = 50;
            if (sched_setscheduler (0, SCHED_RR, &shdprm) == -1)
                perror ("SCHED_SETSCHEDULER_1");
            execl("son", "son", NULL);
        }

    if(close(fdrd) != 0)
        perror("Closing file");

    system("ps -o f,s,pid,ppid,cls,pri,ni,stat,cmd,rtprio xf > proc.txt");
    for (i = 0; i < 2; i++)
        printf("Процесс с pid = %d завершен\n", wait(&status));
    return 0;
}