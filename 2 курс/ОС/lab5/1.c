#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>


static void sigHandler(int sig) {
    printf("Caught signal %s\n", sig == SIGUSR1 ? "SIGUSR1" : "SIGUSR2");
    printf("Parent = %d\n", getppid());
    // Restore the old disposition
    signal(sig, SIG_DFL);
}

int main() {
    printf("\nFather started: pid = %i, ppid = %i\n", getpid(), getppid());

    signal(SIGUSR1, sigHandler);
    signal(SIGUSR2, sigHandler);
    signal(SIGINT, SIG_DFL);
    signal(SIGCHLD, SIG_IGN);

    int forkRes = fork();

    if (forkRes == 0) {
        // Child process
        printf("\nSon started: pid = %i, ppid = %i\n", getpid(), getppid());

        // Send signals to parent
        if (kill(getppid(), SIGUSR1) != 0) {
            printf("Error while sending SIGUSR1\n");
            exit(1);
        }
        printf("Successfully sent SIGUSR1\n");

        return 0;
    }

    // Parent process
    wait(NULL); // Wait for child to finish

    for (;;) {
        pause(); // Wait for signals
    }

    return 0;
}

