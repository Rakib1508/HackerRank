#include <iostream>
#include <cstdio>

int max_of_four (int w, int x, int y, int z) {
    if (w > x) {
        if (w > y) {
            if (w > z) {
                return w;
            }
            else {
                return z;
            }
        }
        else {
            if (y > z) {
                return y;
            }
            else {
                return z;
            }
        }
    }
    else {
        if (x > y) {
            if (x > z) {
                return x;
            }
            else {
                return z;
            }
        }
        else {
            if (y > z) {
                return y;
            }
            else {
                return z;
            }
        }
    }
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
