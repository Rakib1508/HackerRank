#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    scanf("%d\n", &n);
    
    int numbers[n];
    int sum = 0;
    int i;
    
    for (i = 0; i < n; i++) {
        scanf("%d ", &numbers[i]);
        sum += numbers[i];
    }
    
    printf("%d\n", sum);
    
    return 0;
}
