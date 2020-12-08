#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int find_nth_term(int n, int a, int b, int c) {
    int list[n];
    int index;
    list[0] = a;
    list[1] = b;
    list[2] = c;
    
    for (index = 3; index < n; index++) {
        list[index] = list[index-1] + list[index-2] + list[index-3];
    }
    return list[n-1];
}

int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}
