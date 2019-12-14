#include <stdio.h>

long E(long a, long b)
{
    long t, result = 0;

    while (b) {
        t = b;
        b = a % b;
        a = t;
        result++;
    }
    return result;
}

long S(long N)
{
    long x, y, sum = 0;
    for (x = 1; x <= N; x++)
        for (y = 1; y <= N; y++)
            sum += E(x, y);
    return sum;
}

int main(void)
{
    printf("%ld\n", E(1, 1));
    printf("%ld\n", E(10, 6));
    printf("%ld\n", E(6, 10));
    printf("%ld\n", S(1));
    printf("%ld\n", S(10));
    printf("%ld\n", S(100));
    printf("%ld\n", S(5000000));
    return 0;
}
