#include <stdio.h>

int main()
{
    int pid = getpid();
    int ppid = getppid();
    printf("\n\nSON PARAMS: pid=%i ppid=%i\n\n",pid,ppid);
    sleep(2);
    return 0; // статус завершения 0
}
