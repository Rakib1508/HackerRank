#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
  	char *list[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int i;
    for (i = a; i <= b; i++) {
        if (i>=0 && i<10) {
            printf("%s\n", list[i]);
        }
        else if (i%2 == 0) {
            printf("even\n");
        }
        else {
            printf("odd\n");
        }
    }
    return 0;
}
