#include <unistd.h>
#include <stdlib.h>
int main(int argc, char * argv[]) {
    char* file = "ls";
    char* path = "/bin/ls";
    char *args[] = {"ls", "-l", NULL };
    char * env[] = { (char*)NULL };
    int pid = fork();
    if (pid == 0) {
    switch ( (int)argv[1][0] ) {
        case (int)'1':
            execl("/bin/ls", "/bin/ls", "-l", (char *)NULL);break;
        case (int)'2':
            execlp("ls", "ls", "-l", (char *)NULL); break;
        case (int)'3':
            execle("/bin/ls", "ls", "-l", (char *)NULL, env); break;
        case (int)'4':
            execv("/bin/ls", args); break;
        case (int)'5':
            execvp("ls", args); break;
        case (int)'6':
            execvpe("ls", args, (char *)NULL, env); break;
    }
    }
}
