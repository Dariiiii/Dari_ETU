#include <stdio.h>
#include <stdlib.h>

int main()
{
    int pid = getpid();
    int ppid = getppid();
    printf("SON PARAMS: pid=%i ppid=%i\n",pid,ppid);
    sleep(15);
    exit(1); 
}
