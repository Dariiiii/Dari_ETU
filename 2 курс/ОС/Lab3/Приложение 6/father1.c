#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <wait.h>
int main()
{
   int stat, code = 200;
   pid_t pid[6];

   for (int index = 0; index < 6; index++) 
   {
        if((pid[index] = fork()) == 0)  // создаем 6 дочерних
        {                               // процессов
            sleep(3);
            exit(code + index);     // возвращаем код завершения 
        }
   }

   for (int index = 0; index < 6; index++)
   {
        pid_t cpid = waitpid(pid[index], &stat, 0); // отслеживаем
        if(WIFEXITED(stat))
            printf("Child %d is finished with status: %d\n",
            cpid, WEXITSTATUS(stat));
   }
   return 0;
} 
