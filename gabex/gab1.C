#include <stdio.h>
#include "gab2.H"

char *atoi(s)
char *s;
{
    int i, n;
    n = 0;
    for (i = 0; *(s+i) >= '0' && *(s+i) <= '9'; ++i) {
        n = 10 * n + *(s+i) - '0';
    }
    return(n);
}

void insertion_sort(arr, n)
int arr[];
int n;
{
    int i, j, temp;
    for (i=1; i<n; i++)
    {
        temp = arr[i];
        j = i-1;
        while((temp < arr[j]) && (j>=0))
        {
            arr[j+1] = arr[j];
            j = j-1;
        }
        arr[j+1] = temp;
    }
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
