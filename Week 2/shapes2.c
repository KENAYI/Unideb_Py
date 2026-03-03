#include <stdio.h>
#include <stdlib.h>

int main()
{
    double a, b;
    scanf("%lf %lf", &a, &b);
    printf("%.2lf %.2lf \n", a, b);
    printf("%.3lf \n", a * b);

    return 0;
}