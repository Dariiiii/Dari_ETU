#include <fcntl.h>
#include <sys/mman.h>
#include <sys/resource.h>
#include <sched.h>

int main(int argc, char *argv[])
{
    int pid, ppid;

    pid = getpid();
    ppid = getppid();

    int pr = getpriority(PRIO_PROCESS, pid);
    printf("son params: pid = %i ppid = %i priority = %i\n",pid,ppid,pr);

    sleep(2);

    return 0;
}