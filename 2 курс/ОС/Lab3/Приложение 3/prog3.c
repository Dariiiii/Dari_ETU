#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sched.h>

const int COLUMN = 70;
const int ROW = 850;

int main()
{
    int pid, a = 255, b = 1, prod = 0;
    int all = 200, index = 0;
    char pid_str[20], ppid_str[20], count_str[4];

    struct sched_param shdprm;
    char **output;       // массив для сохранения в оперативной памяти
    output = (char **) malloc( ROW * sizeof (char *));
    for(int i = 0; i < ROW; i++)
    {
        output[i] = (char *) malloc(COLUMN * sizeof (char));
    }

    pid = fork();
    if (pid == -1)
    {
        perror("fork");
        exit(1);
    }

    shdprm.sched_priority = 50; // изменяем политику и приоритет планирования для доч. процесса
    if (sched_setscheduler (pid, SCHED_RR, &shdprm) == -1) {
        perror ("SCHED_SETSCHEDULER");
    }

    shdprm.sched_priority = 30; // изменяем политику и приоритет планирования для род. процесса
    if (sched_setscheduler (0, SCHED_RR, &shdprm) == -1) {
        perror ("SCHED_SETSCHEDULER");
    }
    while(all)
    {
        sprintf(count_str, "%d", all);
        sprintf(pid_str, "%d", getpid());
        sprintf(ppid_str, "%d", getppid());
        if (pid != 0) // потомок
        {
            char temp[70] = "count new = ";
            strcat(temp, count_str);
            strcat(temp, " , new pid = ");
            strcat(temp, pid_str);
            strcat(temp, " , ppid = ");
            strcat(temp, ppid_str);
            strcat(temp, "\n");
            strcpy(output[index], temp);
        }
        else        // родитель
        {
            char temp[70] = "count parent = ";
            strcat(temp, count_str);
            strcat(temp, " , parent pid = ");
            strcat(temp, pid_str);
            strcat(temp, " , ppid = ");
            strcat(temp, ppid_str);
            strcat(temp, "\n");
            strcpy(output[index], temp);
        }

        prod = a + b - a;   // вычисления
        index++;
        all--;
    }

    for(int y = 0; y < ROW; y++)    // итоговый вывод на экран
    {
        for(int x = 0; x < COLUMN; x++)
        {
            printf("%c", output[y][x]);
        }
        printf("\n");
    }
    
    system("ps xf -Fc > proc.txt");

    printf("Завершение процесса\n");
    exit(1);
}
