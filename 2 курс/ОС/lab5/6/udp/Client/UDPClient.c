#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "Utility.h"

int main(int argc, char *argv[])
{
    int sock;                        /* Socket descriptor */
    struct sockaddr_in echoServAddr; /* Echo server address */
    struct sockaddr_in fromAddr;     /* Source address of echo */
    unsigned short echoServPort;     /* Echo server port */
    unsigned int fromSize;           /* In-out of address size for recvfrom() */
    char *servIP;                    /* IP address of server */
    char sendString[BUF_SIZE];                /* String to send to echo server */
    char reciveString[BUF_SIZE];      /* Buffer for receiving echoed string */


    if ((argc < 2) || (argc > 3))    /* Test for correct number of arguments */
    {
        fprintf(stderr,"Usage: %s <Server IP> <Echo Port>\n", argv[0]);
        exit(1);
    }

    servIP = argv[1];           /* First arg: server IP address (dotted quad) */
    echoServPort = atoi(argv[2]);       /* Second arg: string to echo */

    /* Create UDP socket */
    if ((sock = socket(PF_INET, SOCK_DGRAM, IPPROTO_UDP)) < 0)
        Error("socket creature is failed");

    memset(&echoServAddr, 0, sizeof(echoServAddr));     /* Zero out structure */
    echoServAddr.sin_family = AF_INET;                          /* Internet addr family */
    echoServAddr.sin_addr.s_addr = inet_addr(servIP);       /* Server IP address */
    echoServAddr.sin_port   = htons(echoServPort);     /* Server port */

    for(;;)
    {
        printf("Input request (empty to exit)\n");
        bzero(sendString, BUF_SIZE);

        fgets(sendString, BUF_SIZE, stdin);
        sendString[strlen(sendString) - 1] = '\0';

        if(strlen(sendString) == 0) {
            printf("Bye-bye\n");
            break;
        }

        if (sendto(sock, sendString, BUF_SIZE, 0, (struct sockaddr *)
                &echoServAddr, sizeof(echoServAddr)) != BUF_SIZE)
            Error("sendto() sent a different number of bytes than expected\n");


        fromSize = sizeof(fromAddr);
        if ((recvfrom(sock, reciveString, BUF_SIZE, 0,
                                      (struct sockaddr *) &fromAddr, &fromSize)) != BUF_SIZE)
            Error("recvfrom() failed");

        if(fromAddr.sin_addr.s_addr != echoServAddr.sin_addr.s_addr)
        {
            printf("Error: received a packet from unknown source.\n");
        }


        printf("Received: %s len=%d\n", reciveString, BUF_SIZE);

    }
    close(sock);
    exit(0);
}
