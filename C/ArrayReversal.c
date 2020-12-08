#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d\n", &n);
    
    int num[n], reversed[n];
    int i, j;
    
    for (i = 0; i < n; i++) {
        scanf("%d ", &num[i]);
        reversed[n - i - 1] = num[i];
    }
    
    for (j = 0; j < n; j++) {
        printf("%d ", reversed[j]);
    }
}
