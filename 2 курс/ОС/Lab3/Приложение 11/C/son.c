#include <fcntl.h>
#include <sys/mman.h>
#include <sched.h>

int main(int argc, char *argv[])
{
    if (mlockall((MCL_CURRENT | MCL_FUTURE)) < 0)
        perror("mlockall error");
    char c;
    int pid, ppid, buf;
    int fdrd = 3;
    int fdwr = 4;

    pid = getpid();
    ppid = getppid();

    printf("son params: pid=%i ppid=%i\n",pid,ppid);

    sleep(5);

    for(;;)
    {
        if (read(fdrd,&c,1) != 1)  // читаем по одному символу,
            {
                return 0;
            }             // пока не закончится файл
        write(fdwr, &c, 1);        // записываем полученный символ в новый файл
        printf("pid = %d: %c\n", pid, c);
    }
    return 0;
}