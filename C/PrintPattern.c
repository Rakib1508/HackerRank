#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define min(a, b) ((a) < (b) ? (a) : (b))

int main() 
{

    int n;
    scanf("%d", &n);
  	
    int length = n * 2 - 1;
    int row, col;
    
    for (row = 0; row < length; row++) {
        for (col = 0; col < length; col++) {
            int m = min(row, col);
            m = min(m, length - row - 1);
            m = min(m, length - col - 1);
            printf("%d ", n - m);
        }
        printf("\n");
    }
    
    return 0;
}
