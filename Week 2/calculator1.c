#include <stdio.h>

int main()
{
    double a, b;
    char op;

    scanf("%lf %c %lf", &a, &op, &b);
    printf("%.3lf %c %.3lf = ", a, op, b); 

    if (op == '+') 
    {
        printf("%.3lf", a + b);
    }

    else if (op == '-') 
    {
        printf("%.3lf", a - b);
    }

    else if (op == '*') 
    {
        printf("%.3lf", a * b);
    }

    else if (op == '/') 
    {
        if (b == 0)
        {
            printf("Cannot divide by 0!");
        }
        else printf("%.3lf", a / b);
    }

    else printf("Invalid operator!");

    return 0;
}