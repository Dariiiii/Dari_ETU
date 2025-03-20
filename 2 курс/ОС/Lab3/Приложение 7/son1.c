#include <stdio.h>

int main()
{
    int pid = getpid();
    int ppid = getppid();
    printf("SON PARAMS: pid=%i ppid=%i\n",pid,ppid);
    sleep(15);
    return 0;
}
