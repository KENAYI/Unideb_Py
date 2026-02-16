#include <stdio.h>
#include <stdlib.h>

#define SUCCESS 0
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a,b) ((a) < (b) ? (a) : (b))

int main()
{
    printf("Hello World!\n");
    printf("%d\n", MIN(5,2));
    printf("%d\n", MAX(5,2));

    return SUCCESS;
}