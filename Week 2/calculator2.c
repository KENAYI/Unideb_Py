#include <stdio.h>

int main(void)
{
    double a, b; //DOUBLE DA % OPERATOR CALISMAZ!! SADECE INT!!!!
    char op;

    scanf("%lf %c %lf", &a, &op, &b);
    printf("%.3lf %c %.3lf = ", a, op, b);

    switch(op)
    {
        case '+':
            printf("%.3lf", a + b);
            break;

        case '-':
            printf("%.3lf", a - b);
            break;

        case '*':
            printf("%.3lf", a * b);
            break;

        case '/':
            if (b == 0){
                printf("Cannot divide by 0!");
            }
            else printf("%.3lf", a / b);
            break;

        default:
            printf("\nInvalid operator!");
    }

    return 0;
}