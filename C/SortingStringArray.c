#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return strcmp(b, a);
}

int unique_chars (const char *a) {
    int distinct = 0;
    int list[26] = {0};
    int ascii;
    
    while (*a != '\0') {
        ascii = (*a++) - 'a';
        if (ascii < 26) {
            list[ascii] += 1;
        }
    }
    
    for (int index = 0; index < 26; index++) {
        if (list[index] > 0) {
            distinct += 1;
        }
    }
    
    return distinct;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int result = unique_chars(a) - unique_chars(b);
    return (result) ? result : lexicographic_sort(a, b);
}

int sort_by_length(const char* a, const char* b) {
    return (strlen(a) - strlen(b)) ? strlen(a) - strlen(b) : lexicographic_sort(a, b);
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    int sorted = 0;
    int end = len - 1;
    
    while (!sorted) {
        sorted = 1;
        for (int i = 0; i < end; i++) {
            if (cmp_func(arr[i], arr[i+1]) > 0) {
                char *temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                sorted = 0;
            }
        }
        end -= 1;
    }
}
