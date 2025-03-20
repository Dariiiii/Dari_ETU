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
    char pid_str[20], ppid_str[20], count_str[4];   // временные строки для
                                                    // для дальнейшего сохранения
                                                    // информации
    char **output;      // массив для сохранения в оперативной памяти
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

    while(all)
    {
        sprintf(count_str, "%d", all);      // переводим
        sprintf(pid_str, "%d", getpid());   // счетчик, pid и ppid
        sprintf(ppid_str, "%d", getppid()); // в строки
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

        prod = a + b - a;       // вычисления
        index++;
        all--;
    }

    for(int y = 0; y < ROW; y++)        // вывод на экран 
    {
        for(int x = 0; x < COLUMN; x++)
        {
            printf("%c", output[y][x]);
        }
        printf("\n");
    }

    printf("Завершение процесса\n");
    exit(1);
}
