//
// Created by leksil on 19.04.23.
//
#include <stdio.h>  /* for perror() */
#include <stdlib.h> /* for exit() */
#define BUF_SIZE 100
#define DEFAULT_PORT 8888

void Error(char *errorMessage)
{
    perror(errorMessage);
    exit(1);
}
