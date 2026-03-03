#include <stdio.h>
#include <stdlib.h>

int main() {
        while(1) {
        /*    int left, right;
            char op;
            
            int tmp = scanf("%d %c %d", &left, &op, &right);
            printf("%d\n", tmp);
            if(tmp == EOF) {
                break;
            }
        } */ 

        int left, right;
        char op;

        if(scanf("%d %c %d", &left, &op, &right) == EOF) {
            break;
        }

        switch(op) {
            case '+': printf("%d\n", left + right); break;
            case '-': printf("%d\n", left - right); break;
            case '*': printf("%d\n", left * right); break;
            case '/': printf("%d\n", left / right); break;
            default: printf("Invalid operator\n");
        }
    }
    
    return EXIT_SUCCESS;
}
