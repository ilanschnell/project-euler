/* two algorithms, they are both very slow, althought S2 is much faster */
#include <stdio.h>
#include "assert.h"

long LIMIT = 10000; // 5000000;
long sum = 0;       /* updated in explore */

long E(long a, long b)
{
    long t, res = 0;

    while (b) {
        t = b;
        b = a % b;
        a = t;
        res++;
    }
    return res;
}

long S1()
{
    long x, y, res = 0;

    for (x = 1; x <= LIMIT; x++)
        for (y = 1; y <= LIMIT; y++)
            res += E(x, y);
    return res;
}

void explore(long x, long y, long steps)
{
    long z;

    assert(0 <= y && y < x && x <= LIMIT);
    sum += steps;
    for (int z = y + (y > 0 ? 1: 2) * x; z <= LIMIT; z += x)
        explore(z, x, steps + 1);
}

long S2()
{
    long i;

    for (i = 1; i <= LIMIT; i++)
        explore(i, 0, 0);
    return sum * 2 + LIMIT * (LIMIT + 1) / 2;
}

int main(void)
{
    printf("%ld\n", S1());
    printf("%ld\n", S2());
    return 0;
}
