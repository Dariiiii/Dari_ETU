#include <stdio.h>

int main(int argc, char * argv[])
{
    int pid = getpid();
    int ppid = getppid();
    printf("SON2 PARAMS: pid=%i ppid=%i\n",pid,ppid);
    for (int i = 0; i < argc; i++)
        printf("argv[%d]: %s\n", i, argv[i]);

    //sleep(2);
    //exit(1); статус завершения 256
    return 0; // статус завершения 0
}
