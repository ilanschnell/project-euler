#include <stdio.h>

/* return Collatz chain length for given start value */
long chain_len(long n)
{
    int result = 0;

    while (n != 1) {
        n = n % 2 ? 3 * n + 1 : n / 2;
        result++;
    }
    return result;
}

int main(void)
{
    long m = 0;                 /* max chain length */
    long result;
    long i, k;

    for (i = 1; i < 1000000; i++) {
        k = chain_len(i);
        if (k > m) {
            m = k;
            result = i;
        }
    }
    printf("%ld\n", result);

    return 0;
}
