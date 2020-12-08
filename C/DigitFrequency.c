#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int arr[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};    
    char string[1000];
    scanf("%s", string);
    int len = strlen(string);
    
    for (int i = 0; i < len; i++) {
        int index = string[i] - '0';
        if (index >= 0 && index <= 9) {
            arr[index] += 1;
        }
    }
    
    for (int x = 0; x < 10; x++) {
        printf("%d ", arr[x]);
    }
    
    return 0;
}
