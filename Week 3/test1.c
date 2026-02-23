#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);

    for(int i=0; i<n; i++) {
        int left, right;
        char op;
        scanf("%d %c %d", &left, &op, &right);
        //printf("%d %c %d\n", left, op, right);

        if(op == '+') {
            printf("%d\n", left + right);
        }

        if(op == '-') {
            printf("%d\n", left - right);
        }

        if(op == '*') {
            printf("%d\n", left * right);
        }

        
        if(op == '/') {
            printf("%d\n", left / right);
        }

        if(op == '%') {
            printf("%d\n", left % right);
        }
    }

    return EXIT_SUCCESS;
}