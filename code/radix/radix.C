#include <stdio.h>
#include "radix.H"

void counting_sort(arr, n, exp)
int arr[];
int n;
int exp;
{
    int i, output[100], count[10];
    
    for (i = 0; i < 10; i++)
        count[i] = 0;
    
    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
    
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
    
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    
    for (i = 0; i < n; i++)
        arr[i] = output[i];
}

void radix_sort(arr, n)
int arr[];
int n;
{
    int i, max, exp;
    
    max = arr[0];
    for (i = 1; i < n; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    
    for (exp = 1; max / exp > 0; exp *= 10)
        counting_sort(arr, n, exp);
}

int atoi(s)
char *s;
{
    int i, n;
    n = 0;
    for (i = 0; *(s+i) >= '0' && *(s+i) <= '9'; ++i) {
        n = 10 * n + *(s+i) - '0';
    }
    return(n);
}

void fileArray(arr, f, n) 
int arr[];
int n;
FILE *f;
{
    int i;
    char linbuff[MAXLINE];
    for (i=0; i<n; i++) {
        fgets(linbuff, MAXLINE, f);
        arr[i] = atoi(linbuff);
    }
}
