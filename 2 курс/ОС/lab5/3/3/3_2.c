#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#define NUM_SIGNALS 5

void handle_rt_signal(int sig, siginfo_t* info, void* context) 
{
    printf("Handling real-time signal %d\n", sig);
    usleep(100000);
}

void handle_normal_signal(int sig) 
{
    printf("Handling normal signal %d\n", sig);
    if (sig == SIGINT)
    {
        signal(sig, SIG_DFL);
    }
    usleep(100000);
}

int main() 
{
    printf("Father pid = %d ppid = %d\n", getpid(), getppid());
    struct sigaction sa_rt;
    sa_rt.sa_sigaction = handle_rt_signal;
    sa_rt.sa_flags = SA_SIGINFO;
    sigemptyset(&sa_rt.sa_mask);
    for (int i = SIGRTMIN; i <= SIGRTMAX; i++) 
    {
        sigaction(i, &sa_rt, NULL);
    }
    // Register normal signals
    for (int i = 1; i <= NUM_SIGNALS; i++) 
    {
        signal(i, handle_normal_signal);
    }
    // Send signals
    if (fork() == 0)
    {
        printf("Son pid = %d ppid = %d\n", getpid(), getppid());
        printf("Son sending signals to father...\n");
        for (int i = 1; i <= NUM_SIGNALS; i++) 
        {
            printf("Sending normal signal %d\n", i);
            kill(getppid(), i);
        }
        for (int i = SIGRTMAX; i >= SIGRTMIN; --i) 
        {
            printf("Sending real-time signal %d\n", i);
            kill(getppid(), i);
        }
        printf("Signals sent. Sleeping for 5 seconds to allow handling...\n");
        sleep(3);
        return 0;
    }
    for (;;)
    {
        pause();
    }
    return 0;
}
