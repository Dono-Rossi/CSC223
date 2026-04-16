#include "BDSCTEST.H"
#include "gab2.H"

main() {
    START_TESTING("gab3.C");
    TEST_CASE("Sorting given list") {
        int arr[7];
        int n;
        n = 7;
        arr[0] = 3;
        arr[1] = 2;
        arr[2] = 6;
        arr[3] = 5;
        arr[4] = 1;
        arr[5] = 4;
        arr[6] = 7;
        insertion_sort(arr, n);
        ASSERT(arr[0], 1);
        ASSERT(arr[1], 2);
        ASSERT(arr[2], 3);
        ASSERT(arr[3], 4);
        ASSERT(arr[4], 5);
        ASSERT(arr[5], 6);
        ASSERT(arr[6], 7);
    }
    TEST_CASE("Opening a file") {
        int arr2[5];
        FILE *f;
        int n2;
        n2 = 5;
        f = fopen("LIST.TXT", "r");
        fileArray(arr2, f, n2);
        ASSERT(arr2[0], 1);
        ASSERT(arr2[1], 2);
        ASSERT(arr2[2], 3);
        ASSERT(arr2[3], 4);
        ASSERT(arr2[4], 5);
        fclose(f);
    }
    TEST_CASE("Putting those together") {
        int arr3[5];
        FILE *f2;
        int n3;
        n3 = 5;
        f2 = fopen("LIST.TXT", "r");
        fileArray(arr3, f2, n3);
        insertion_sort(arr3, n3);
        ASSERT(arr3[0], 1);
        ASSERT(arr3[1], 2);
        ASSERT(arr3[2], 3);
        ASSERT(arr3[3], 4);
        ASSERT(arr3[4], 5);
        fclose(f2);
    }
    TEST_CASE("Putting it all together") {
        int arr4[5];
        FILE *f3;
        int n4;
        n4 = 5;
        int counter;
        f3 = fopen("LIST.TXT", "r");
        fileArray(arr4, f3, n4);
        insertion_sort(arr4, n4);
        fclose(f3);
        f3 = fopen("LIST.TXT", "w");
        for (counter=0; counter<n4; counter++) {
            fprintf(f3, "%d\n", arr4[counter]);
        }
        fclose(f3);
        f3 = fopen("LIST.TXT", "r");
        fileArray(arr4, f3, n4);
        ASSERT(arr4[0], 1);
        ASSERT(arr4[1], 2);
        ASSERT(arr4[2], 3);
        ASSERT(arr4[3], 4);
        ASSERT(arr4[4], 5);
        fclose(f3);
    }


    END_TESTING();
}
