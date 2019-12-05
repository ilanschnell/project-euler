from numba import njit

LIMIT = 10_000_000

@njit
def main():
    a = [0 for i in range(LIMIT + 1)]

    for i in range(2, LIMIT // 2):
        for j in range(i, LIMIT, i):
            a[j] += 1

    result = 0
    for i in range(2, LIMIT):
        if a[i] == a[i + 1]:
            result += 1
    print(result)

main()
