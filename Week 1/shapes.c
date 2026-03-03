#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a;
    printf("Enter the side a!\n");
    scanf("%d", &a);
    printf("Side a is %d\n", a);

    int b;
    printf("Enter the side b!\n");
    scanf("%d", &b);
    printf("Side b is %d\n", b);

    printf("Area is %d\n", a * b);

    return 0;
}