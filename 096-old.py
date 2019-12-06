from copy import deepcopy

Result = 0

def solve(S):

    def options(i, j):
        r = list(S[i])
        r.extend(S[k][j] for k in range(9))
        r.extend(S[i//3 * 3 + k][j//3 * 3 + m]
                 for k in range(3) for m in range(3))
        s = set(r)
        return [z for z in range(1, 10) if z not in list(s)]

    mnp = 99
    mp = None
    for i in range(9):
        for j in range(9):
            if S[i][j] == 0:
                p = options(i, j)
                if len(p) < mnp:
                    mnp = len(p)
                    mp = i, j, p
    if mp == None:
        global Result
        Result += 100 * S[0][0] + 10*S[0][1] + S[0][2]
        return

    T = deepcopy(S)
    i, j, p = mp
    W = []
    for c in p:
        T[i][j] = c
        W.append(solve(T))
    for c in W:
        return c

fi = open('files/p096_sudoku.txt','r')
for grid in range(50):
    if fi.readline()[0:4] != 'Grid':
        raise 'Error while reading.'
    M = []
    for j in range(9):
        M.append([int(c) for c in fi.readline().strip()])
    solve(M)

print(Result)
