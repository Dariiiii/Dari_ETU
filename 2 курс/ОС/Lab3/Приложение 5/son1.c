#include <stdio.h>

int main()
{
    int pid = getpid();
    int ppid = getppid();
    printf("SON1 PARAMS: pid=%i ppid=%i\n",pid,ppid);
    //sleep(2);
    //exit(1); статус завершения 256
    return 0; // статус завершения 0
}
